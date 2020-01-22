# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-21 22:35
from __future__ import unicode_literals

from django.db import migrations

def load_initial_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "initial_data")


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0012_0_8_3')
    ]

    operations = [
        migrations.RunPython(load_initial_from_fixture),
    ]
