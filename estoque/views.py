from rest_framework.viewsets import ModelViewSet

from .models import Categoria, Fornecedor, Produto
from .serializers import (CategoriaSerializer, FornecedorSerializer,
                          ProdutoSerializer)


class ProdutoAPIViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaAPIViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FornecedorAPIViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
