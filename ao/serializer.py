from .models import Aos
from rest_framework import serializers
class AoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aos
        fields = '__all__'