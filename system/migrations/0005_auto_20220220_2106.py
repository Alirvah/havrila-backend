# Generated by Django 2.1.8 on 2022-02-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_antik_fup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antik_fup',
            name='date',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
