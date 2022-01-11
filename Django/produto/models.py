# Título: Produto
# Descrição: Classe produto
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

import alvo
from django.db import models

from alvo.models import Alvo


class Produto(Alvo):
    modelo=models.CharField(max_length=255)
    marca=models.CharField(max_length=255)
    cod_barra=models.CharField(max_length=255)
    peso=models.DecimalField(max_digits=8,decimal_places=2)
    altura=models.DecimalField(max_digits=8,decimal_places=2)
    data_validade=models.DateField()
    data_fabricacao=models.DateField()
    imagem=models.CharField(max_length=255)

    def cadProduto(self):
        pass
