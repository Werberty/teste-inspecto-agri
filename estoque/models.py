from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=165)
    numero = models.CharField(max_length=65)
    bairro = models.CharField(max_length=165)
    cidade = models.CharField(max_length=165)


class Fornecedor(Endereco):
    nome_fantasia = models.CharField(max_length=165)
    razao_social = models.CharField(max_length=165)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome_fantasia


class Telefone(models.Model):
    numero = models.CharField(max_length=11)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, related_name='telefones')

    def __str__(self):
        return self.numero


class FornecedorPreco(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    preco_de_custo = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.fornecedor} - R$ {self.preco_de_custo}'


class Categoria(models.Model):
    nome = models.CharField(max_length=165, unique=True)
    data_de_criacao = models.DateField(auto_now_add=True)
    data_de_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco_dos_fornecedores = models.ManyToManyField(FornecedorPreco)
    data_de_criacao = models.DateField(auto_now_add=True)
    data_de_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
