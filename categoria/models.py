# Título: Categoria
# Descrição: Classe categoria do módulo movimento
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Categoria(models.Model):
    nome=models.CharField(max_length=255)
    tipo=models.CharField(max_length=255)
    descricao=models.TextField()

    def cadCategoria(self):
        pass
