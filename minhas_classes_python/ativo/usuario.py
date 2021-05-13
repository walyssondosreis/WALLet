# Título: Usuário
# Descrição: Classe de usuários do sistema
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8
from django.db import models
from django.db.models.fields import AutoField

class Usuario(models.Model):
    id=""
    nome=""
    data_nasc=""
    __carteira=""

    def __init__(self,nome):
        self.nome=nome

    def login(self):
        pass
