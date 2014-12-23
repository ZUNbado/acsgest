# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0007_facturaexterna_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaexterna',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
