# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0004_auto_20141213_2317'),
        ('es', '0004_auto_20141213_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='es',
            name='moviment',
            field=models.ForeignKey(blank=True, to='caixa.Moviment', null=True),
            preserve_default=True,
        ),
    ]
