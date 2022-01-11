# Título: Serviço
# Descrição: Classe servico do módulo movimento
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models
from alvo.models import Alvo


class Servico(Alvo):
    tipo=models.CharField(max_length=255)
    tempo_estimado=models.TimeField()

    def cadServico(self):
        pass