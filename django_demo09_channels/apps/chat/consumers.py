from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 'room_name'从URL路由中获取参数chat/routing.py，打开与消费者的websocket连接
        # 每个使用者都有一个范围，其中包含有关其他连接的信息
        # 特别是包括URL路由中的任何位置关键字参数以及当前经过身份验证的用户
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # 直接从用户指定的房间构造Channels组名称，不进行任何引用或转义
        # 组名只能包含字母，数字，连字符和句号
        # 因此，如果输入具有其他字符的房间名将失败
        self.room_group_name = 'chat_{}'.format(self.room_name)

        # 进入房间
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # 接受websocket连接
        # 如果不在connect（）方法中调用accept（），则拒绝并关闭
        # 如果您选择接受连接，建议将accept()作为connect()中的最后一个操作调用
        await self.accept()
    
    async def disconnect(self, close_code):
        # 离开房间
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """ 从websocket接收消息 """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # # 发消息到WebSocket
        # await self.send(text_data=json.dumps({
        #     'message':message
        # }))
        # 发送消息到房间
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        """ 从房间接收消息 """
        message = event['message']

        # 发消息到websocket
        await self.send(text_data=json.dumps({
            'message': message
        }))