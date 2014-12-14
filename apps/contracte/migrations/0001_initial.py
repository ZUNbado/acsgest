# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tercer', '0001_initial'),
        ('servei', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentari', models.CharField(max_length=200, null=True, blank=True)),
                ('multi', models.IntegerField(default=1)),
                ('descompte', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('alta', models.DateField(null=True, blank=True)),
                ('actiu', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=20)),
                ('periode', models.IntegerField(default=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contracte',
            name='periode',
            field=models.ForeignKey(to='contracte.Periode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contracte',
            name='serveis',
            field=models.ManyToManyField(to='servei.Servei'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contracte',
            name='tercer',
            field=models.ForeignKey(to='tercer.Tercer'),
            preserve_default=True,
        ),
    ]
