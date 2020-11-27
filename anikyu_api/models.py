from django.db import models

class Anime(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    poster_image = models.TextField(max_length=150)
    background_image = models.TextField(max_length=150)
    categories = models.TextField(max_length=300, null=True)
    rating = models.FloatField()
    start_date = models.DateField()

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
    anime_count = models.IntegerField(default=0)

    watched_animes = models.ManyToManyField(Anime, related_name="watched_animes")
    wanted_animes = models.ManyToManyField(Anime, related_name="wanted_animes")
    unwanted_animes = models.ManyToManyField(Anime, related_name="unwanted_animes")