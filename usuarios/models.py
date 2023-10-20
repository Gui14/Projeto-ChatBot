from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

class info_cadastro (models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    endereco = models.CharField(max_length=300)
    bairro = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    nome_guardiao = models.CharField(max_length=200)
    email_guardiao = models.EmailField()
    telefone_guardiao = models.CharField(max_length=15)
    


