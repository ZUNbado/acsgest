# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0002_auto_20141213_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='es',
            name='referencia',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
