# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0006_facturaexterna_tercer'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaexterna',
            name='pdf',
            field=models.FileField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
