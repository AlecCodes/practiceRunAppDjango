# Generated by Django 4.1.6 on 2023-02-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='time',
            field=models.IntegerField(),
        ),
    ]
