from django.db import models
from tache.models import Taches
# Create your models here.
class Postes(models.Model):
    code=models.CharField(max_length=100)
    description=models.TextField()
    tache = models.ForeignKey(Taches, on_delete=models.CASCADE)