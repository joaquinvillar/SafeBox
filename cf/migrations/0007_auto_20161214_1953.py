# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cf', '0006_auto_20161214_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='document',
            field=models.FileField(null=True, upload_to='static/cf/documents/'),
        ),
    ]
