# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0003_caixa_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moviment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=200)),
                ('quantitat', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('caixa_desti', models.ForeignKey(related_name='caixadesti', to='caixa.Caixa')),
                ('caixa_origen', models.ForeignKey(related_name='caixaorigen', to='caixa.Caixa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='caixa',
            name='total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
