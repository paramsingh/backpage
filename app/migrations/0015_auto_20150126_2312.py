# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20150126_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
