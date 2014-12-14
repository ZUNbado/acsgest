# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0002_auto_20141213_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixa',
            name='total',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
