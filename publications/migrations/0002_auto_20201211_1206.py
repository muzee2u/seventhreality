# Generated by Django 3.1.4 on 2020-12-11 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchpaper',
            name='publishDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]