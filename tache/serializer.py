from .models import Taches
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class TacheSerializer(ModelSerializer):
    class Meta:
        model = Taches
        fields = '__all__'