# Título: Carteira
# Descrição: Classe de carteiras do usuário
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Carteira(models.Model):
    nome=models.CharField(max_length=255)
    tipo=models.CharField(max_length=255)
    frase_anual=models.TextField()
    #agent_fin=""
    #transacao=""
    #saldo=""
    #divida=""
    #poupanca=""
    #ganho=""
    #gasto=""
    ultima_interacao=models.DateField()

    def cadCarteira(self):
        pass
    
    def abrirCarteira(self):
        pass


