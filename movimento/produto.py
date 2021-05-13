# Título: Produto
# Descrição: Classe produto do módulo movimento
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from movimento.alvo import Alvo


class Produto(Alvo):
    modelo=""
    marca=""
    cod_barra=""
    peso=""
    altura=""
    validade=""
    fabricacao=""
    imagem=""

    def __init__(self):
        pass
