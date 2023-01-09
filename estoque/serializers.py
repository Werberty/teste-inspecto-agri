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
            'id', 'produto',
            'fornecedor', 'fornecedor_name',
            'preco_de_custo',
        ]

    fornecedor_name = serializers.StringRelatedField(
        source='fornecedor', read_only=True)


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao',
            'categoria', 'categoria_name',
            'preco_nos_fornecedores',
            'preco_nos_fornecedores_objects',
            'data_de_criacao', 'data_de_atualizacao',
        ]

    categoria_name = serializers.StringRelatedField(
        source='categoria', read_only=True)

    preco_nos_fornecedores_objects = FornecedorPrecoSerializer(
        many=True, read_only=True, source='preco_nos_fornecedores')


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'id', 'nome_fantasia', 'razao_social', 'cnpj',
            'telefones', 'telefones_objects', 'produtos',  'produtos_objects',
            'logradouro', 'numero', 'bairro', 'cidade'
        ]

    produtos_objects = serializers.StringRelatedField(
        many=True, source='produtos', read_only=True)
    telefones_objects = serializers.StringRelatedField(
        many=True, read_only=True, source='telefones')
