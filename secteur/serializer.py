from .models import Secteurs
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class SecteurSerializer(ModelSerializer):
    class Meta:
        model = Secteurs
        fields = '__all__'