from rest_framework import serializers

from .models import Categoria, Fornecedor, FornecedorPreco, Produto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id', 'nome', 'data_de_criacao', 'data_de_atualizacao'
        ]


class FornecedorPrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorPreco
        fields = [
            'id', 'fornecedor', 'preco_de_custo',
        ]


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'categoria',
            'data_de_criacao', 'data_de_atualizacao', 'preco_dos_fornecedores'
        ]

    preco_dos_fornecedores = FornecedorPrecoSerializer(
        many=True, read_only=True)


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'id', 'nome_fantasia', 'razao_social', 'cnpj',
            'logradouro', 'numero', 'bairro', 'cidade'
        ]
