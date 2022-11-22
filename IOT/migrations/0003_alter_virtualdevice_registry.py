# Generated by Django 4.1.3 on 2022-11-17 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IOT', '0002_alter_virtualdevice_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualdevice',
            name='registry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vds', to='IOT.registry'),
        ),
    ]
