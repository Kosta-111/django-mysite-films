from django.db import models
from datetime import datetime

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    year = models.IntegerField(default=datetime.today().year)
    author = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    imageUrl = models.URLField(blank=True)
    budget = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.genre}), {self.year}y."
