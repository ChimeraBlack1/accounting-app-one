# Generated by Django 3.0.5 on 2020-04-17 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_auto_20200417_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_bal',
            new_name='account_balance',
        ),
    ]