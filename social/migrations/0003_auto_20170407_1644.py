# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_instagramuser_linkedinuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]