from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('login/', views.logar, name="login"),
]

