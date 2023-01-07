from rest_framework import serializers

from .models import Produto

# class CategoriaSerializer(serializers.Serializer):
#     nome = serializers.CharField(max_length=165)
#     # data_de_criacao = serializers.DateTimeField(auto_now_add=True)
#     # data_de_atualizacao = serializers.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nome


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'categoria',
            'data_de_criacao', 'data_de_atualizacao'
        ]

    categoria = serializers.StringRelatedField()


# class EnderecoSerializer(serializers.Serializer):
#     logradouro = serializers.CharField(max_length=165)
#     numero = serializers.CharField(max_length=65)
#     bairro = serializers.CharField(max_length=165)
#     cidade = serializers.CharField(max_length=165)


# class FornecedorSerializer(EnderecoSerializer):
#     nome_fantasia = serializers.CharField(max_length=165)
#     razao_social = serializers.CharField(max_length=165)
#     cnpj = serializers.CharField(max_length=18)
#     produtos = serializers.ManyToManyField(
#         ProdutoSerializer, related_name='fornecedores')

#     def __str__(self):
#         return self.nome_fantasia


# class TelefoneSerializer(serializers.Serializer):
#     numero = serializers.CharField(max_length=11)
#     fornecedor = serializers.ForeignKey(
#         FornecedorSerializer, on_delete=serializers.CASCADE,
#         related_name='telefones')

#     def __str__(self):
#         return self.numero
