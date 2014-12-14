# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tercer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantitat', models.IntegerField()),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('comentari', models.CharField(max_length=200)),
                ('tercer', models.ForeignKey(blank=True, to='tercer.Tercer', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
