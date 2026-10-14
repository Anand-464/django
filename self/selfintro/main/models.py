from django.db import models
class Movies(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=10)
    rating = models.CharField(max_length=1)