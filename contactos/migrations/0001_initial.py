# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=30)),
                ('fechanacimiento', models.DateField()),
                ('numerodepie', models.IntegerField()),
            ],
        ),
    ]
