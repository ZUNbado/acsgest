# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=80)),
                ('preu', models.DecimalField(max_digits=5, decimal_places=2)),
                ('last', models.BooleanField(default=True)),
                ('anterior', models.ForeignKey(blank=True, to='servei.Servei', null=True)),
                ('categoria', models.ForeignKey(to='servei.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
