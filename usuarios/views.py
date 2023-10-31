from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import info_cadastro
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def cadastrar(request):
    if request.method == "GET":
        return render (request, 'register.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        nome_guardiao = request.POST.get('nome_guardiao')
        email_guardiao = request.POST.get('email_guardiao')
        telefone_guardiao = request.POST.get('telefone_guardiao')

        if len(senha) <= 5:
            messages.add_message(request, constants.ERROR, 'A senha deverá conter 6 caracteres ou mais' )
            return redirect('/usuarios/cadastro/')
        
        if info_cadastro.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, "Este email já possui cadastro")
            return redirect('/usuarios/cadastro/')
        else:
            user_= info_cadastro(
                username=nome,
                email = email,
                senha = senha,
                endereco = endereco,
                bairro = bairro,
                telefone = telefone,
                nome_guardiao = nome_guardiao,
                email_guardiao = email_guardiao,
                telefone_guardiao = telefone_guardiao
            )
            user = User.objects.create_user(
                username=email,
                password = senha,
                email=email,
            )
            user_.save()
           
        return redirect('/usuarios/login/')

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username= email, password= senha)

        if user:
            login(request, user)
						# Acontecerá um erro ao redirecionar por enquanto, resolveremos nos próximos passos
            return redirect('/nome_site/inicio')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/usuarios/login')