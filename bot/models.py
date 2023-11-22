from django.db import models

class conversa(models.Model):
    pergunta = models.CharField(max_length=1000)
    resposta = models.CharField(max_length=1000)

class relato_fala(models.Model):
    codinome = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    relato = models.CharField(max_length=1000)