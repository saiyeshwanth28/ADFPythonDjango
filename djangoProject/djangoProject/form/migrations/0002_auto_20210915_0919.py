# Generated by Django 3.2.7 on 2021-09-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='Current_city',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='form',
            name='DOb',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='form',
            name='Nationality',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='form',
            name='Qualification',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='form',
            name='State',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='form',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='form',
            name='pan_number',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='form',
            name='pin_code',
            field=models.CharField(default=None, max_length=6),
        ),
        migrations.AddField(
            model_name='form',
            name='salary',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
