from rest_framework import serializers
from .models import Auteur, Livre, Emprunt

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'


class LivreSerializer(serializers.ModelSerializer):
    auteur_nom = serializers.ReadOnlyField(source='auteur.nom')

    class Meta:
        model = Livre
        fields = '__all__'


class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'