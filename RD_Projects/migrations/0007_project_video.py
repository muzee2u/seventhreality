# Generated by Django 3.1.4 on 2021-06-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RD_Projects', '0006_auto_20210618_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='images/Project_videos'),
        ),
    ]
