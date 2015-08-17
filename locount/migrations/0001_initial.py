# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField(default=0.0)),
                ('longtitude', models.FloatField(default=0.0)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
