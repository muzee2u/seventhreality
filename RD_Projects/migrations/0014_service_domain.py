# Generated by Django 3.1.4 on 2021-07-08 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RD_Projects', '0013_servicedomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RD_Projects.servicedomain'),
        ),
    ]