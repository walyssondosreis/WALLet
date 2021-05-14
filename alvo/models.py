# Create your models here.
# Título: Alvo
# Descrição: Classe alvo
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models
from categoria.models import Categoria

class Alvo(models.Model):
    nome=models.CharField(max_length=255)
    categoria=models.ManyToManyField(Categoria)

    def cadAlvo(self):
        pass