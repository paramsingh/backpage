# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150115_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='submitter',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
