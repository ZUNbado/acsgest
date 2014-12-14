# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tercer', '0002_auto_20141213_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('cognoms', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=15)),
                ('correu', models.EmailField(max_length=200)),
                ('django_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('tercer', models.ForeignKey(blank=True, to='tercer.Tercer', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
