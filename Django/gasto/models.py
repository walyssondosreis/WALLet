# Título: Gasto
# Descrição: Classe gasto do módulo analise
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Gasto(models.Model):
    gasto_atual=models.DecimalField(max_digits=8,decimal_places=2)
    gasto_mensal=models.DecimalField(max_digits=8,decimal_places=2)
    gasto_anual=models.DecimalField(max_digits=8,decimal_places=2)

    def atualizarGasto(self):
        pass

    def consultarGasto(self):
        pass
    
    def gerarGrafico(self):
        pass