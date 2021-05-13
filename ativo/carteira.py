# Título: Carteira
# Descrição: Classe de carteiras do usuário
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

class Carteira:
    __id=""
    nome=""
    tipo=""
    frase_anual=""
    __agent_fin=""
    __transacao=""
    __saldo=""
    __divida=""
    __poupanca=""
    __ganho=""
    __gasto=""
    __ultima_interacao=""

    def __init__(self,nome):
        self.nome=nome
    
    def abrirCarteira(self):
        pass


