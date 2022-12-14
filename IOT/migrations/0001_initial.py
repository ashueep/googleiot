# Generated by Django 4.1.3 on 2022-11-17 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organization', '0006_alter_org_options_alter_proj_org'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.proj')),
            ],
        ),
        migrations.CreateModel(
            name='VirtualDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('temp', models.IntegerField()),
                ('blood_sugar', models.FloatField()),
                ('heater', models.BooleanField()),
                ('registry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vds', to='IOT.registry')),
            ],
        ),
    ]
