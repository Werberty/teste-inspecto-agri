from django.urls import path

from estoque import views

urlpatterns = [
    path('api/', views.api, name='api')
]
