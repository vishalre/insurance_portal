# Generated by Django 2.1.7 on 2019-04-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_userprofile_licenseplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otpgenerator',
            fields=[
                ('mailid', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('otp', models.IntegerField()),
            ],
        ),
    ]