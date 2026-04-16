from rest_framework import viewsets
from .models import Auteur, Livre, Emprunt
from .serializers import AuteurSerializer, LivreSerializer, EmpruntSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

    @action(detail=True, methods=['get'])
    def livres(self, request, pk=None):
        auteur = self.get_object()
        livres = auteur.livres.all()
        serializer = LivreSerializer(livres, many=True)
        return Response(serializer.data)


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        livres = Livre.objects.filter(disponible=True)
        serializer = LivreSerializer(livres, many=True)
        return Response(serializer.data)


class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer