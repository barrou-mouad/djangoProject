from .models import Prixs
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class PrixSerializer(ModelSerializer):
    class Meta:
        model = Prixs
        fields = '__all__'