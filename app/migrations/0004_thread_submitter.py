# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150115_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='submitter',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
    ]
