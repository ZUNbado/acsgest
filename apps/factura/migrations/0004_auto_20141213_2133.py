# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0003_auto_20141213_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturainterna',
            name='referencia',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
