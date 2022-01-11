# Título: Valor
# Descrição: Classe valor 
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models

class Valor(models.Model):
    tipo=models.CharField(max_length=255)
    quantia=models.DecimalField(max_digits=8,decimal_places=2)
    moeda=models.CharField(max_length=255)
    parcelamento=models.CharField(max_length=255)
    
    def cadValor(self):
        pass
