from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto
from .serializers import ProdutoSerializer


@api_view()
def produto_api_view(request):
    produto = Produto.objects.all()
    serializer = ProdutoSerializer(instance=produto, many=True)
    return Response(serializer.data)
