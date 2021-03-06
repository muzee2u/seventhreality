# Generated by Django 3.1.4 on 2020-12-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/Staff_Pics')),
                ('facebook_id', models.CharField(blank=True, default='https://www.facebook.com/', max_length=255, null=True)),
                ('twitter_id', models.CharField(blank=True, default='https://twitter.com/?lang=en', max_length=255, null=True)),
                ('linkedin_id', models.CharField(blank=True, default='https://www.linkedin.com/feed/', max_length=255, null=True)),
            ],
        ),
    ]
