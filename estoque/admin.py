from django.contrib import admin

from .models import Categoria, Fornecedor, Produto, Telefone


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ...


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    ...


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    ...
