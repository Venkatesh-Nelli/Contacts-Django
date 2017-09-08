# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 09:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplelogin', '0004_contact_details_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='contact_number',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999999999999999)]),
        ),
    ]
