# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='es',
            options={'verbose_name': 'Entrada/Sortida', 'verbose_name_plural': 'Entrades/Sortides'},
        ),
        migrations.AddField(
            model_name='es',
            name='quantitat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
