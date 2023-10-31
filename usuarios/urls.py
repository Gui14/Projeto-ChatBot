from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('login/', views.logar, name="login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="redefinir.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="acessoEmail.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="redefinicao.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="acessarLogin.html"), name='password_reset_complete'),
]

