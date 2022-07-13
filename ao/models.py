from django.db import models

# Create your models here.
class Aos(models.Model):
    ref=models.CharField(max_length=100)
    objet=models.TextField()
    region=models.CharField(max_length=200)
    province=models.CharField(max_length=200)
