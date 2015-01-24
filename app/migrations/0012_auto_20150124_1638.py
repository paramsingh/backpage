# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_postreport_threadreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreport',
            name='message',
            field=models.CharField(default='', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='threadreport',
            name='message',
            field=models.CharField(default='', max_length=500),
            preserve_default=True,
        ),
    ]
