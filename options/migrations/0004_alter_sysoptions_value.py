# Generated by Django 3.2.9 on 2022-04-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0003_migrate_languages_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysoptions',
            name='value',
            field=models.JSONField(),
        ),
    ]
