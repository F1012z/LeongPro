# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('LeongGoodsApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('array', models.IntegerField(default=0, auto_created=321456)),
                ('pubdate', models.DateTimeField(default=datetime.datetime(2018, 5, 27, 10, 33, 54, 870118))),
                ('isbuy', models.CharField(default='未付款', max_length=50)),
                ('money', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('isshow', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=1)),
                ('money', models.CharField(default=0, max_length=10)),
                ('isorder', models.BooleanField(default=0)),
                ('isbuy', models.BooleanField(default=0)),
                ('isdelete', models.BooleanField(default=0)),
                ('isgo', models.BooleanField(default=0)),
                ('good', models.ForeignKey(to='LeongGoodsApp.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=60)),
                ('uemail', models.EmailField(max_length=254)),
                ('uaddress', models.CharField(default='', max_length=100)),
                ('uphone', models.CharField(default='', max_length=11)),
                ('ureceiveUser', models.CharField(default='', max_length=20)),
                ('uzip_code', models.CharField(default='', max_length=6)),
                ('ugender', models.BooleanField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='usercart',
            name='user',
            field=models.ForeignKey(to='UserApp.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(to='UserApp.UserInfo'),
        ),
    ]
