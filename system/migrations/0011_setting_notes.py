# Generated by Django 2.1.8 on 2022-05-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
