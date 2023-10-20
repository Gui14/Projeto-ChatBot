from django.urls import path, include
from . import views

urlpatterns = [
    path('aila/', views.aila, name='aila'),
    path('faq/', views.faq, name='faq'),
    path('inicio/', views.inicio, name='inicio'),
    
]

