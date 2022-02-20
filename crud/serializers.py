from .models import Atleta
from rest_framework import serializers

class AtletaCreationSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=100)
    equipe = serializers.CharField(max_length=100)
    genero = serializers.CharField(max_length = 50)
    peso = serializers.IntegerField()
    idade = serializers.IntegerField()
    graduacao = serializers.CharField(max_length = 50)
    class Meta():
        model = Atleta
        fields = ['id', 'nome','equipe','genero','peso','idade','graduacao']

class AtletaDetailSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=100)
    equipe = serializers.CharField(max_length=100)
    genero = serializers.CharField(max_length = 50)
    peso = serializers.IntegerField()
    idade = serializers.IntegerField()
    graduacao = serializers.CharField(max_length = 50)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    class Meta():
        model = Atleta
        fields = ['id','nome','equipe','genero','peso','idade','graduacao','created_at','updated_at']

