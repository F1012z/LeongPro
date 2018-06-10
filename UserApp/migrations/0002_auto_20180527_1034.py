# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 27, 10, 34, 0, 965567)),
        ),
    ]
