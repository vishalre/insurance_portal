# Generated by Django 2.1.7 on 2019-04-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0008_otpgenerator'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsmodel',
            name='damagedpart',
            field=models.CharField(default='test', max_length=10),
        ),
    ]
