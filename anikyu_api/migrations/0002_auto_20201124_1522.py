# Generated by Django 3.1.3 on 2020-11-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anikyu_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
