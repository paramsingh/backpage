# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_thread_post_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.GenericIPAddressField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='poster',
            field=models.GenericIPAddressField(null=True),
            preserve_default=True,
        ),
    ]
