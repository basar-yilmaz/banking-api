# Generated by Django 4.2.3 on 2023-07-28 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankingApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='id',
            new_name='account_id',
        ),
    ]
