from django.db import models

# Create your models here.
class Secteurs(models.Model):
    code=models.CharField(max_length=100)
    description=models.TextField()