# Generated by Django 3.1.4 on 2021-07-09 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RD_Projects', '0015_project_content1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='content1',
        ),
    ]
