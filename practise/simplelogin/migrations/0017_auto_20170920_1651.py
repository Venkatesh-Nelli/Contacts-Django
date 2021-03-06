# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simplelogin', '0016_auto_20170919_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254),
        ),
    ]
