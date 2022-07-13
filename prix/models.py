from django.db import models
from poste.models import Postes
# Create your models here.
class Prixs(models.Model):
    code=models.CharField(max_length=100)
    description=models.TextField()
    unite=models.IntegerField()
    poste = models.ForeignKey(Postes, on_delete=models.CASCADE)

 