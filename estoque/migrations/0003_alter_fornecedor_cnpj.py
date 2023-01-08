# Generated by Django 4.1.5 on 2023-01-07 18:14

from django.db import migrations, models
import estoque.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_alter_fornecedorpreco_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(max_length=18, validators=[estoque.validators.valida_cnpj]),
        ),
    ]