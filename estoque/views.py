from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoAPIViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# class ProdutoAPILista(ListCreateAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer


# class ProdutoAPIDetalhe(RetrieveUpdateDestroyAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer
