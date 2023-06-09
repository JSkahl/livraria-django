from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from livraria.models import Editora
from livraria.serializers.editora import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer