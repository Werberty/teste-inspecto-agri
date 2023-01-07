from django.urls import include, path
from rest_framework.routers import SimpleRouter

from estoque import views

app_name = 'estoque'

produto_api_router = SimpleRouter()
produto_api_router.register(
    'produtos/api',
    views.ProdutoAPIViewSet,
    basename='produtos-api'
)

categoria_api_router = SimpleRouter()
categoria_api_router.register(
    'categorias/api',
    views.CategoriaAPIViewSet,
    basename='categorias-api'
)

fornecedores_api_router = SimpleRouter()
fornecedores_api_router.register(
    'fornecedores/api',
    views.FornecedorAPIViewSet,
    basename='fornecedores-api'
)


urlpatterns = [
    path('', include(produto_api_router.urls)),
    path('', include(categoria_api_router.urls)),
    path('', include(fornecedores_api_router.urls)),
]
