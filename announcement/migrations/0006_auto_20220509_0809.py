# Generated by Django 3.2.9 on 2022-05-09 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0005_friendshiplinks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ('-order', '-create_time')},
        ),
        migrations.AddField(
            model_name='announcement',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
