# Generated by Django 3.2.7 on 2021-09-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20210915_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestform',
            name='DOb',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
