# Título: Operação
# Descrição: Classe operacao
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models
from django.db.models.deletion import CASCADE
from valor.models import Valor
from alvo.models import Alvo

class Operacao(models.Model):
    status=models.CharField(max_length=255)
    datah_ini=models.DateTimeField()
    datah_fim=models.DateTimeField()
    datah_ag=models.DateTimeField()
    valor=models.OneToOneField(Valor,on_delete=CASCADE,default="")
    alvo=models.ManyToManyField(Alvo)

    def cadOperacao(self):
        pass
