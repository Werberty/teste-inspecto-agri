from rest_framework.viewsets import ModelViewSet

from ..models import Categoria, Fornecedor, FornecedorPreco, Produto
from ..serializers import (CategoriaSerializer, FornecedorPrecoSerializer,
                           FornecedorSerializer, ProdutoSerializer)


class ProdutoAPIViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaAPIViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FornecedorAPIViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class FornecedorPrecoAPIViewSet(ModelViewSet):
    queryset = FornecedorPreco.objects.all()
    serializer_class = FornecedorPrecoSerializer
