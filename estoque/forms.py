from django import forms

from .models import Categoria, Fornecedor, FornecedorPreco, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome'
        ]


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = [
            'nome',
            'descricao',
            'categoria',
        ]
        widgets = {
            'descricao': forms.Textarea(
                attrs={
                    'rows': '2'
                }
            )
        }


class FornecedorPrecoForm(forms.ModelForm):
    class Meta:
        model = FornecedorPreco
        fields = [
            'fornecedor',
            'preco_de_custo'
        ]


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nome_fantasia',
            'razao_social',
            'cnpj',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
        ]
