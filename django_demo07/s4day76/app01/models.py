from django.db import models

# Create your models here.
class tempChannelData(models.Model):
    """
    临时通道数据信息，用户查询的时候临时保存到数据库，当超过400条，删除前200条记录
    nid, key:shot_channel, value: shot, channel, isHaveData(?), 
    xAis{len,start,end}, yAis, yInfo{min,max,unit}, shotTime(记得转str), createdTime
    """
    nid = models.BigAutoField(primary_key=True)
    shot_channel = models.CharField(max_length=32)
    shot = models.IntegerField()
    channel = models.CharField(max_length=32)
    isHaveData = models.BooleanField()
    xAis = models.CharField(max_length=64)
    yAis = models.TextField()
    # yAis = models.CommaSeparatedIntegerField()
    yInfo = models.CharField(max_length=64)
    shotTime = models.CharField(max_length=32)
    createdTime = models.DateTimeField(auto_now_add = True)
