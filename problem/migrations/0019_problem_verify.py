# Generated by Django 3.2.9 on 2022-05-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0018_problemanswer_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='verify',
            field=models.BooleanField(default=True),
        ),
    ]
