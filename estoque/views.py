from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto
from .serializers import ProdutoSerializer


@api_view(http_method_names=['get', 'post'])
def produto_api_lista(request):
    if request.method == 'GET':
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(
            instance=produto,
            many=True
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(http_method_names=['get', 'patch', 'delete'])
def produto_api_detalhe(request, pk):
    produto = get_object_or_404(
        Produto.objects.all(),
        pk=pk
    )
    if request.method == 'GET':
        serializer = ProdutoSerializer(
            instance=produto,
            many=False,
            context={'request': request}
        )
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ProdutoSerializer(
            instance=produto,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data
        )
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
