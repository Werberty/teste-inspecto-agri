from rest_framework.viewsets import ModelViewSet

from ..models import Categoria, Fornecedor, FornecedorPreco, Produto, Telefone
from ..serializers import (CategoriaSerializer, FornecedorPrecoSerializer,
                           FornecedorSerializer, ProdutoSerializer,
                           TelefoneSerializer)


class ProdutoAPIViewSet(ModelViewSet):
    queryset = Produto.objects.all().select_related('categoria')
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


class TelefoneAPIViewSet(ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
