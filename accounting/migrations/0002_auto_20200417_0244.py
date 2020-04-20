# Generated by Django 3.0.5 on 2020-04-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.CharField(default='A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(default='A', max_length=1),
        ),
    ]