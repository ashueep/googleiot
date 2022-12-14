# Generated by Django 4.1.3 on 2022-11-17 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IOT', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='virtualdevice',
            options={'permissions': (('assign_device', 'assigns device to registry'),)},
        ),
        migrations.AlterField(
            model_name='virtualdevice',
            name='blood_sugar',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='virtualdevice',
            name='heater',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='virtualdevice',
            name='registry',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vds', to='IOT.registry'),
        ),
        migrations.AlterField(
            model_name='virtualdevice',
            name='temp',
            field=models.IntegerField(blank=True),
        ),
    ]
