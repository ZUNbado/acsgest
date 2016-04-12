# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tercer', '0002_auto_20141213_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='tercer',
            name='actiu',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tercer',
            name='colectiu',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
