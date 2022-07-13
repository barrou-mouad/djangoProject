from django.db import models
from ao.models import Aos
from prix.models import Prixs
# Create your models here.
class Ao_Prix(models.Model):
    pu=models.FloatField()
    qty=models.IntegerField()
    ao = models.ForeignKey(Aos, on_delete=models.CASCADE)
    prix = models.ForeignKey(Prixs, on_delete=models.CASCADE)
