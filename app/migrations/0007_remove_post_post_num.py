# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_thread_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_num',
        ),
    ]
