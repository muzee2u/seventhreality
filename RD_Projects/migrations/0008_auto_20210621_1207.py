# Generated by Django 3.1.4 on 2021-06-21 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RD_Projects', '0007_project_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='voucher',
            field=models.ImageField(blank=True, null=True, upload_to='images/Project_vouchers'),
        ),
        migrations.AddField(
            model_name='project',
            name='voucherPDF',
            field=models.ImageField(blank=True, null=True, upload_to='images/Project_voucherPDF'),
        ),
    ]
