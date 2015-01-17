# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_post_post_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='submitter',
        ),
    ]
