from django.shortcuts import render


def produtos_view(request):
    return render(request, 'estoque/produtos.html')
