# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0004_auto_20141213_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturainterna',
            name='descompte',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
