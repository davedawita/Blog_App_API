from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Body = models.TextField()
