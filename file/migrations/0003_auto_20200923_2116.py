# Generated by Django 2.1.8 on 2020-09-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20200923_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filer',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='filer',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
