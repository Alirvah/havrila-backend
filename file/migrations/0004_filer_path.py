# Generated by Django 2.1.8 on 2020-10-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20200923_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='filer',
            name='path',
            field=models.TextField(default='unknown'),
            preserve_default=False,
        ),
    ]
