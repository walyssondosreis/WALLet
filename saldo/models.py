# Título: Saldo
# Descrição: Classe saldo
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Saldo(models.Model):
    saldo_atual=models.DecimalField(max_digits=8,decimal_places=2)
    saldo_mensal=models.DecimalField(max_digits=8,decimal_places=2)

    def atualizarSaldo(self):
        pass

    def consultarSaldo(self):
        pass
    
    def gerarGrafico(self):
        pass
