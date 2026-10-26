from django.db import models

class Note(models.Model):
    user = models.TextField()
    title = models.CharField(max_length=10)
    message = models.TextField()