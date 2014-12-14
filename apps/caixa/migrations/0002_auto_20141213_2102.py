# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caixa',
            options={'verbose_name_plural': 'Caixes'},
        ),
        migrations.AlterModelOptions(
            name='tipus',
            options={'verbose_name_plural': 'Tipus'},
        ),
    ]
