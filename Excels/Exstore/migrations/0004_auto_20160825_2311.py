# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-25 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exstore', '0003_auto_20160823_1635'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userdata',
            unique_together=set([('first_name', 'last_name', 'age', 'gender', 'address')]),
        ),
    ]
