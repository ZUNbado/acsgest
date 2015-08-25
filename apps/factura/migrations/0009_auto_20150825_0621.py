# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0008_auto_20141223_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaexterna',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'factures', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facturainterna',
            name='pagat',
            field=models.DecimalField(default=0, null=True, max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
