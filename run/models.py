from django.db import models

# Create your models here.

class Run(models.Model):
    name = models.CharField(max_length=100)
    distance = models.IntegerField()
    time = models.DurationField()