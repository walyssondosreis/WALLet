# Título: Carteira
# Descrição: Classe de carteiras do usuário
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models
from django.db.models.deletion import CASCADE
from banco.models import Banco
from transacao.models import Transacao
from saldo.models import Saldo
from divida.models import Divida
from poupanca.models import Poupanca
from ganho.models import Ganho
from gasto.models import Gasto

class Carteira(models.Model):
    nome=models.CharField(max_length=255)
    tipo=models.CharField(max_length=255)
    frase_anual=models.TextField()
    ultima_interacao=models.DateField()
    agent_fin=models.ManyToManyField(Banco)
    transacao=models.ForeignKey(Transacao,on_delete=CASCADE,default="")
    saldo=models.ForeignKey(Saldo,on_delete=CASCADE,default="")
    divida=models.ForeignKey(Divida,on_delete=CASCADE,default="")
    poupanca=models.ForeignKey(Poupanca,on_delete=CASCADE,default="")
    ganho=models.ForeignKey(Ganho,on_delete=CASCADE,default="")
    gasto=models.ForeignKey(Gasto,on_delete=CASCADE,default="")
    
    def cadCarteira(self):
        pass
    
    def abrirCarteira(self):
        pass


