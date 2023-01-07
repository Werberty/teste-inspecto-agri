# Generated by Django 4.1.5 on 2023-01-07 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=165, unique=True)),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
                ('data_de_atualizacao', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=165)),
                ('numero', models.CharField(max_length=65)),
                ('bairro', models.CharField(max_length=165)),
                ('cidade', models.CharField(max_length=165)),
            ],
        ),
        migrations.CreateModel(
            name='FornecedorPreco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_de_custo', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('endereco_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='estoque.endereco')),
                ('nome_fantasia', models.CharField(max_length=165)),
                ('razao_social', models.CharField(max_length=165)),
                ('cnpj', models.CharField(max_length=18)),
            ],
            bases=('estoque.endereco',),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
                ('data_de_atualizacao', models.DateField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.categoria')),
                ('fornecedor', models.ManyToManyField(to='estoque.fornecedorpreco')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefones', to='estoque.fornecedor')),
            ],
        ),
        migrations.AddField(
            model_name='fornecedorpreco',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.fornecedor'),
        ),
    ]
