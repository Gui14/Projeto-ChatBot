from django.db import models

class conversa(models.Model):
    pergunta = models.CharField(max_length=1000)
    resposta = models.CharField(max_length=1000)
