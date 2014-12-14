# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_auto_20141213_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturainterna',
            name='quantitat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
