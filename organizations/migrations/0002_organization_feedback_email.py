# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='feedback_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
