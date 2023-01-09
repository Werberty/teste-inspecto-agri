from django.forms.models import inlineformset_factory
from django.shortcuts import render

from estoque.forms import (CategoriaForm, FornecedorForm, FornecedorPrecoForm,
                           ProdutoForm, TelefoneForm)
from estoque.models import Fornecedor, FornecedorPreco, Produto, Telefone


def produtos_view(request):
    if request.method == 'GET':
        form = ProdutoForm()
        form_fornecedor_preco_factory = inlineformset_factory(
            Produto, FornecedorPreco, form=FornecedorPrecoForm, extra=1
        )
        form_fornecedor_preco = form_fornecedor_preco_factory()
        context = {
            'form': form,
            'form_fornecedor_preco': form_fornecedor_preco
        }
        return render(request, 'estoque/pages/produtos.html', context)


def categoria_view(request):
    form = CategoriaForm()
    return render(request, 'estoque/pages/categorias.html', context={
        'form': form
    })


def fornecedor_view(request):
    if request.method == "GET":
        form_telefone_facatory = inlineformset_factory(
            Fornecedor, Telefone, form=TelefoneForm, extra=1
        )
        form_telefone = form_telefone_facatory()
        form = FornecedorForm()
        return render(request, 'estoque/pages/fornecedores.html', context={
            'form': form,
            'form_telefone': form_telefone
        })
