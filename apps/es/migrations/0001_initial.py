# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('donacio', '0001_initial'),
        ('caixa', '0001_initial'),
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ES',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrada', models.BooleanField(default=True)),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('comentari', models.CharField(max_length=200, null=True, blank=True)),
                ('caixa', models.ForeignKey(to='caixa.Caixa')),
                ('donacio', models.ForeignKey(blank=True, to='donacio.Donacio', null=True)),
                ('factura_externa', models.ForeignKey(blank=True, to='factura.FacturaExterna', null=True)),
                ('factura_interna', models.ForeignKey(blank=True, to='factura.FacturaInterna', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
