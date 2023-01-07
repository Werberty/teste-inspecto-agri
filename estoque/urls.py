from django.urls import path

from estoque import views

urlpatterns = [
    path('api/', views.ProdutoAPILista.as_view(), name='produto_api_list'),
    path('api/<int:pk>', views.ProdutoAPIDetalhe.as_view(),
         name='produto_api_detalhe')
]
