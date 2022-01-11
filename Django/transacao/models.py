# Título: Transação
# Descrição: Classe transacao
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models
from django.db.models.deletion import CASCADE
from operacao.models import Operacao
from agente.models import Agente

class Transacao(models.Model):
    tipo=models.CharField(max_length=255)
    operacao=models.ForeignKey(Operacao,on_delete=CASCADE,default="")
    agente=models.OneToOneField(Agente,on_delete=CASCADE,primary_key=True, default="")
    comprovante=models.CharField(max_length=255)
    
    def realizarTransacao(self):
        pass
