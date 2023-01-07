import re

from django.core.exceptions import ValidationError


def valida_cnpj(cnpj):
    novo_cnpj = remover_caracteres(cnpj)

    if len(novo_cnpj) < 12:
        raise ValidationError('Caracteres inválidos')

    if eh_sequencia(novo_cnpj):
        raise ValidationError('Não permite sequência')

    # try:
    primeiro_digito = calcula_primeiro_digito(novo_cnpj)
    novo_cnpj.append(primeiro_digito)
    segundo_digito = calcula_segundo_digito(novo_cnpj)
    novo_cnpj.append(segundo_digito)
    novo_cnpj = formata_cnpj(novo_cnpj)
    # except:
    #     return ValidationError('CNPJ inválido')

    if novo_cnpj != cnpj:
        raise ValidationError('CNPJ inválido')


def calcula_primeiro_digito(cnpj):
    lista1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_total = 0
    for i in range(len(lista1)):
        multiplica = cnpj[i] * lista1[i]
        soma_total += multiplica
    resultado = 11 - (soma_total % 11)
    if resultado > 9:
        return 0
    else:
        return resultado


def calcula_segundo_digito(cnpj):
    lista1 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_total = 0
    for i in range(len(lista1)):
        multiplica = cnpj[i] * lista1[i]
        soma_total += multiplica
    resultado = 11 - (soma_total % 11)
    if resultado > 9:
        return 0
    else:
        return resultado


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def remover_caracteres(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    cnpj = [int(n) for n in cnpj]
    return cnpj[:12]


def formata_cnpj(cnpj):
    cnpj = ''.join([str(n)for n in cnpj])
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'


if __name__ == '__main__':
    cnpj = '25.903.308/0001-78'
    valida = valida_cnpj(cnpj)
    print(valida)
