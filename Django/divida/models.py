# Título: Dívida
# Descrição: Classe divida
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Divida(models.Model):
    divida_atual=models.DecimalField(max_digits=8,decimal_places=2)
    divida_mensal=models.DecimalField(max_digits=8,decimal_places=2)
    divida_anual=models.DecimalField(max_digits=8,decimal_places=2)

    def atualizarDivida(self):
        pass

    def consultarDivida(self):
        pass
    
    def gerarGrafico(self):
        pass
