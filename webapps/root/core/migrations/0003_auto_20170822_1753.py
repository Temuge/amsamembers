# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170819_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_domain_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='university_assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.University'),
        ),
    ]