from django import forms

from utils.django_forms import add_attr, add_placeholder

from .models import Categoria, Fornecedor, FornecedorPreco, Produto, Telefone


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields['cnpj'], 'CNPJ válido')

        add_attr(self.fields['cnpj'], 'class', 'mask-cnpj')

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


class TelefoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields['numero'], 'Telefone (com DDD)')

        add_attr(self.fields['numero'], 'class', 'mask-phone')

    class Meta:
        model = Telefone
        fields = [
            'numero'
        ]
        labels = {
            'numero': 'Telefone'
        }
