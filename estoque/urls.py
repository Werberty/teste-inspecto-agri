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

print(produto_api_router.urls)

urlpatterns = [
    path('', include(produto_api_router.urls)),
]
