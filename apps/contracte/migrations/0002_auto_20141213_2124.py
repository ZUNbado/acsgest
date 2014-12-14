# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracte',
            name='descompte',
            field=models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
