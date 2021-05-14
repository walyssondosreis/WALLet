# Título: Ganho
# Descrição: Classe ganho do módulo analise
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Ganho(models.Model):
    ganho_atual=models.DecimalField(max_digits=8,decimal_places=2)
    ganho_mensal=models.DecimalField(max_digits=8,decimal_places=2)
    ganho_anual=models.DecimalField(max_digits=8,decimal_places=2)

    def atualizarGanho(self):
        pass

    def consultarGanho(self):
        pass
    
    def gerarGrafico(self):
        pass
