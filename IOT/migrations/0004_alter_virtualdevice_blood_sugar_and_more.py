# Generated by Django 4.1.3 on 2022-11-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IOT', '0003_alter_virtualdevice_registry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualdevice',
            name='blood_sugar',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='virtualdevice',
            name='heater',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='virtualdevice',
            name='temp',
            field=models.IntegerField(default=0),
        ),
    ]
