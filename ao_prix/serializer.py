from .models import Ao_Prix
from rest_framework import serializers
class Ao_PrixSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ao_Prix
        fields = '__all__'