from .models import Phases
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
class PhaseSerializer(ModelSerializer):
    class Meta:
        model = Phases
        fields = '__all__'