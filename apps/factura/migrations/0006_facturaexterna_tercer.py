# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tercer', '0002_auto_20141213_2102'),
        ('factura', '0005_facturainterna_descompte'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaexterna',
            name='tercer',
            field=models.ForeignKey(blank=True, to='tercer.Tercer', null=True),
            preserve_default=True,
        ),
    ]
