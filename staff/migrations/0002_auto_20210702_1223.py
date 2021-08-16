# Generated by Django 3.1.4 on 2021-07-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='facebook_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='linkedin_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='twitter_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='profile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
