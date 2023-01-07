from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoAPILista(APIView):
    def get(self, request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(
            instance=produto,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class ProdutoAPIDetalhe(APIView):
    def get_produto(self, pk):
        produto = get_object_or_404(
            Produto.objects.all(),
            pk=pk
        )
        return produto

    def get(self, request, pk):
        produto = self.get_produto(pk)
        serializer = ProdutoSerializer(
            instance=produto,
            many=False,
            context={'request': request}
        )
        return Response(serializer.data)

    def patch(self, request, pk):
        produto = self.get_produto(pk)
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

    def delete(self, request, pk):
        produto = self.get_produto(pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
