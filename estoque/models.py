from django.db import models

from .validators import valida_cnpj


class Endereco(models.Model):
    logradouro = models.CharField(max_length=165, blank=True, null=True)
    numero = models.CharField(max_length=65, blank=True, null=True)
    bairro = models.CharField(max_length=165, blank=True, null=True)
    cidade = models.CharField(max_length=165, blank=True, null=True)


class Fornecedor(Endereco):
    nome_fantasia = models.CharField(max_length=165)
    razao_social = models.CharField(max_length=165)
    cnpj = models.CharField(max_length=18, validators=[
                            valida_cnpj,], unique=True)

    def __str__(self):
        return self.nome_fantasia


class Telefone(models.Model):
    numero = models.CharField(max_length=14)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, related_name='telefones')

    def __str__(self):
        return self.numero


class Categoria(models.Model):
    nome = models.CharField(max_length=165, unique=True)
    data_de_criacao = models.DateField(auto_now_add=True)
    data_de_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE)
    data_de_criacao = models.DateField(auto_now_add=True)
    data_de_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class FornecedorPreco(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE,
        related_name='preco_nos_fornecedores')
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, related_name='produtos')
    preco_de_custo = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.produto} - R$ {self.preco_de_custo}'
