from django.db import models

# Create your models here.
from LeongGoodsApp.models import *


class UserInfo(models.Model):
    '''
    姓名，密码，邮箱，地址，手机号，收件人 。邮编 ,性别
    '''
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=60)
    uemail = models.EmailField()
    uaddress = models.CharField(max_length=100, default='')
    uphone = models.CharField(max_length=11, default='')
    ureceiveUser = models.CharField(max_length=20, default='')
    uzip_code = models.CharField(max_length=6, default='')
    ugender = models.BooleanField(default=0)


class OrderInfo(models.Model):
    array = models.IntegerField(auto_created=321456, default=0)
    user = models.ForeignKey(UserInfo)
    pubdate = models.DateTimeField(default=datetime.datetime.now())
    isbuy = models.CharField(max_length=50, default='未付款')
    money = models.CharField(max_length=20, default='0')


class UserCart(models.Model):
    user = models.ForeignKey(UserInfo)
    good = models.ForeignKey(GoodsInfo)
    isshow = models.IntegerField(default=0)
    count = models.IntegerField(default=1)
    money = models.CharField(max_length=10, default=0)
    isorder = models.BooleanField(default=0)
    isbuy = models.BooleanField(default=0)
    isdelete = models.BooleanField(default=0)
    isgo = models.BooleanField(default=0)
