# Generated by Django 3.1.4 on 2020-12-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RD_Projects', '0003_delete_subdomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Project_pics'),
        ),
    ]
