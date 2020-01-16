from django.db import models

# Create your models here.
class UserGroup(models.Model):
    """
    部门
    """
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    """
    员工
    """
    nid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)
    ug = models.ForeignKey('UserGroup', on_delete=models.CASCADE, null=True)


class UserType(models.Model):
    """
    用户类型
    """
    title = models.CharField(max_length=32)

class UserInfo2(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType', on_delete=models.CASCADE,)

    def __str__(self):
        return "%s-%s" %(self.id, self.name)