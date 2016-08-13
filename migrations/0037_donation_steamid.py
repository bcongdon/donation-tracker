# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0036_tech_notes_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='steamid',
            field=models.CharField(max_length=64, verbose_name=b'SteamID 64', blank=True),
        ),
    ]
