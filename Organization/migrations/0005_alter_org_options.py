# Generated by Django 4.1.3 on 2022-11-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0004_alter_org_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='org',
            options={'permissions': (('add_user', 'can add user to organization'), ('remove_user', 'can remove user from organization'))},
        ),
    ]
