# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplelogin', '0002_auto_20170902_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_details',
            old_name='name',
            new_name='contact_name',
        ),
        migrations.RenameField(
            model_name='contact_details',
            old_name='number',
            new_name='contact_number',
        ),
    ]
