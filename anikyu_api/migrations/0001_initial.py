# Generated by Django 3.1.3 on 2020-11-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('anime_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField()),
                ('poster_image', models.TextField(max_length=150)),
                ('background_image', models.TextField(max_length=150)),
                ('categories', models.TextField(max_length=300, null=True)),
                ('rating', models.FloatField()),
                ('start_date', models.DateField()),
                ('unwanted_animes', models.ManyToManyField(related_name='unwanted_animes', to='anikyu_api.User')),
                ('wanted_animes', models.ManyToManyField(related_name='wanted_animes', to='anikyu_api.User')),
                ('watched_animes', models.ManyToManyField(related_name='watched_animes', to='anikyu_api.User')),
            ],
        ),
    ]
