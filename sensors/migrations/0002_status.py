# Generated by Django 2.1.8 on 2020-10-04 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('uptime', models.IntegerField()),
                ('cpu', models.IntegerField()),
                ('mem', models.IntegerField()),
                ('disk', models.IntegerField()),
                ('temp', models.IntegerField()),
                ('wrec', models.IntegerField()),
                ('wtran', models.IntegerField()),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
