from django.db import models
from secteur.models import Secteurs
# Create your models here.
class Phases(models.Model):
    code=models.CharField(max_length=100)
    description=models.TextField()
    secteur = models.ForeignKey(Secteurs, on_delete=models.CASCADE)