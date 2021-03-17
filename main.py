# TITLE: WALLet
# DESCRIPTION: Gestão pessoal de finanças.
# AUTHOR: WALYSSON PEREIRA DOS REIS
# CREATE DATA: 21.03.15
# UPDATE DATA: 21.03.15

# coding: utf-8

class PivoAcao:
    """  Estabelecimento ou Pessoa de Origem ou Destino do recurso """
    nome_razao=""
    cpf_cnpj=""
    info=""
    def __init__(self,nr):
        self.nome_razao=nr.upper()
    def BuscaPv(self):
        return [self.nome_razao,self.cpf_cnpj,self.info.upper()]

###################################################

p1=PivoAcao("Medeiros e moura")
p1.cpf_cnpj=35698
p1.info="Supermercado"
print(p1)






