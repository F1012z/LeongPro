# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_auto_20180527_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 27, 10, 36, 27, 929598)),
        ),
    ]
