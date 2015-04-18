# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='sex',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
    ]
