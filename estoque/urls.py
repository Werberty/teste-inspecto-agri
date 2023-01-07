from django.urls import path

from estoque import views

urlpatterns = [
    path('api/', views.produto_api_lista, name='produto_api_list'),
    path('api/<int:pk>', views.produto_api_detalhe,
         name='produto_api_detalhe')
]
