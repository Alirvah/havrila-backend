# Generated by Django 2.1.8 on 2022-05-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20220507_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
