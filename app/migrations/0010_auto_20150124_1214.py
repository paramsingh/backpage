# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_thread_last_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reports',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='reports',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
