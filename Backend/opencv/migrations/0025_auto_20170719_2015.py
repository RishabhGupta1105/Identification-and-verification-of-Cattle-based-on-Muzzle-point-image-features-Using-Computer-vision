# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencv', '0024_remove_cattle_fid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cattle_face_data',
            new_name='cattle_f',
        ),
    ]
