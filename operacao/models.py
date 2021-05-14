# Título: Operação
# Descrição: Classe operacao
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Operacao(models.Model):
    status=models.CharField(max_length=255)
    datah_ini=models.DateTimeField()
    datah_fim=models.DateTimeField()
    datah_ag=models.DateTimeField()
    #valor=""
    #alvo=""

    def cadOperacao(self):
        pass
