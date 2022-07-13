from .models import Postes
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class PostSerializer(ModelSerializer):
    class Meta:
        model = Postes
        fields = '__all__'