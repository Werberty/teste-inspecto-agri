from django import forms

from .models import FornecedorPreco, Produto


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
