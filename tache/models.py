from django.db import models
from phase.models import Phases
# Create your models here.
class Taches(models.Model):
    code=models.CharField(max_length=100)
    description=models.TextField()
    phase = models.ForeignKey(Phases, on_delete=models.CASCADE)