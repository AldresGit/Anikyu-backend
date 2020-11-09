from django.db import models
from . import User

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

    watched_animes = models.ManyToManyField(User)
    wanted_animes = models.ManyToManyField(User)
    unwanted_animes = models.ManyToManyField(User)