# Título: Transação
# Descrição: Classe transacao
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Transacao(models.Model):
    tipo=models.CharField(max_length=255)
    #operacao=""
    #agente=""
    comprovante=models.CharField(max_length=255)
    
    def realizarTransacao(self):
        pass
