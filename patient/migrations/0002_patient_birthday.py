# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
