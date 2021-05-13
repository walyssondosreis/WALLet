# Título: Usuário
# Descrição: Classe de usuários do sistema
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8
from django.db import models

class Usuario(models.Model):
    #id="" # Criado automaticamente pelo django.
    slug=models.SlugField(max_length=255, unique=True)
    nome=models.CharField(max_length=255)
    data_nasc=models.DateField()
    #carteira=""


    def login(self):
        print("Você esta logado amigo!")
        #pass