from .models import Raca
from rest_framework import serializers

class RacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = '__all__'