# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-16 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20170716_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Organization'),
        ),
    ]