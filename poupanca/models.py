# Título: Poupança
# Descrição: Classe poupanca do módulo analise
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Poupanca(models.Model):
    poup_atual=models.DecimalField(max_digits=8,decimal_places=2)
    poup_mensal=models.DecimalField(max_digits=8,decimal_places=2)

    def atualizarPoupanca(self):
        pass

    def consultarPoupanca(self):
        pass
    
    def gerarGrafico(self):
        pass

