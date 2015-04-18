# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20141107_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateField()),
                ('whole_foods', models.IntegerField(default=0)),
                ('processed_foods', models.IntegerField(default=0)),
                ('notes', models.TextField()),
                ('user_profile', models.ForeignKey(to='userprofile.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
