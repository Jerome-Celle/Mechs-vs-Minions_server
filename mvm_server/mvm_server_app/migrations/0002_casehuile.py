# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvm_server_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseHuile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('posX', models.IntegerField()),
                ('posY', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
