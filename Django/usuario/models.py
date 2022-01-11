# Título: Usuário
# Descrição: Classe de usuários do sistema
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8
from django.db import models
from carteira.models import Carteira

class Usuario(models.Model):
    nome=models.CharField(max_length=255)
    data_nasc=models.DateField()
    slug=models.SlugField(max_length=255, unique=True)
    carteira=models.ManyToManyField(Carteira)

    def cadUsuario(self):
        pass

    def login(self):
        pass