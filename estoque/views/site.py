from django.forms.models import inlineformset_factory
from django.shortcuts import render

from estoque.forms import FornecedorPrecoForm, ProdutoForm
from estoque.models import FornecedorPreco, Produto


def produtos_view(request):
    form = ProdutoForm()
    form_fornecedor_preco_factory = inlineformset_factory(
        Produto, FornecedorPreco, form=FornecedorPrecoForm, extra=2
    )
    form_fornecedor_preco = form_fornecedor_preco_factory()
    context = {
        'form': form,
        'form_fornecedor_preco': form_fornecedor_preco
    }
    return render(request, 'estoque/produtos.html', context)


def inserir(request):
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
        return render(request, 'estoque/produtos.html', context)
