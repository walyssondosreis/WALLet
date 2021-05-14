# Título: Banco
# Descrição: Classe de cadastro para agente financeiro
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Banco(models.Model):
    nome=models.CharField(max_length=255)
    tipo_conta=models.CharField(max_length=255)
    num_conta=models.CharField(max_length=255)
    titular_conta=models.CharField(max_length=255)

    def cadBanco(self,nome):
        pass



