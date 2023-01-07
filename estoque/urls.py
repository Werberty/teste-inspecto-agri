from django.urls import path

from estoque import views

urlpatterns = [
    path('api/', views.produto_api_view, name='produto_api_view')
]
