from django import forms

from .models import Categoria, FornecedorPreco, Produto


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


class FornecedorPrecoForm(forms.ModelForm):
    class Meta:
        model = FornecedorPreco
        fields = [
            'fornecedor',
            'preco_de_custo'
        ]
