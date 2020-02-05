from django.db import models
# import time
import json
import requests


# def get_data():
#     url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d' % int( time.time()*1000)
#     data = json.loads(requests.get(url=url).json()['data'])

#     mapAreaList = ["南海诸岛", '北京', '天津', '上海', '重庆', '河北', '河南', '云南', '辽宁', '黑龙江', '湖南', '安徽', '山东', '新疆', '江苏', '浙江', '江西', '湖北', '广西', '甘肃', '山西', '内蒙古', '陕西', '吉林', '福建', '贵州', '广东', '青海', '西藏', '四川', '宁夏', '海南', '台湾', '香港', '澳门', ]

#     # {'country': '中国', 'area': '广东', 'city': '广州', 'confirm': 94, 'suspect': 0, 'dead': 0, 'heal': 0}
#     areaData = {}
#     confirmData = {}
#     for item in data:
#         if item['country'] == '中国':
#             if item['area'] in confirmData:
#                 areaData[item['area']].append(item)
#                 confirmData[item['area']] += item['confirm']
#             else:
#                 areaData[item['area']] = [item,]
#                 confirmData[item['area']] = item['confirm']
    
#     reConfirmData = {}
#     for area in mapAreaList:
#         if area in confirmData:
#             reConfirmData[area] = confirmData[area]
#         else:
#             reConfirmData[area] = 0

#     return [areaData, reConfirmData]

def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data = json.loads(requests.get(url=url).json()['data'])

    return data


def get_news():
	url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_time_line'
	news = json.loads(requests.get(url=url).json()['data'])
    
	return news
