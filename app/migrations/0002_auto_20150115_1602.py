# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_num',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='thread_num',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='thread_pos',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
