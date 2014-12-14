# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contracte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaExterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=200)),
                ('creacio', models.DateField(default=datetime.datetime.now)),
                ('pagament', models.DateField(null=True, blank=True)),
                ('estat', models.BooleanField(default=False)),
                ('quantitat', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('pagat', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('comentari', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FacturaInterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=200)),
                ('creacio', models.DateField(default=datetime.datetime.now)),
                ('pagament', models.DateField(null=True, blank=True)),
                ('estat', models.BooleanField(default=False)),
                ('quantitat', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('pagat', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('comentari', models.CharField(max_length=200, null=True, blank=True)),
                ('contracte', models.ManyToManyField(to='contracte.Contracte')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
