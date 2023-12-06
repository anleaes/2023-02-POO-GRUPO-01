from .models import Ong
from rest_framework import serializers

class OngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']