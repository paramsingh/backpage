# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_thread_thread_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='time',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
