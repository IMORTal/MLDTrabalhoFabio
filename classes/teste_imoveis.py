#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from imoveis import Imoveis, ImovelVendido
from proprietario import Proprietario


class TesteImoveis(unittest.TestCase):
    def teste_criar_imovel(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        imovel = Imoveis(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_atual=p)
        imovel.endereco |should| equal_to("Dr. Manoel Landin 247")
        imovel.bairro |should| equal_to("Alphaville")
        imovel.descricao |should| equal_to("Casa")
        imovel.area |should| equal_to(500.0)

class TesteImovelVendido(unittest.TestCase):

    def teste_criar_imovel_vendido(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        imovel = ImovelVendido(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_atual=p)
        imovel.endereco |should| equal_to("Dr. Manoel Landin 247")
        imovel.bairro |should| equal_to("Alphaville")
        imovel.descricao |should| equal_to("Casa")
        imovel.area |should| equal_to(500.0)
        imovel.proprietario_atual.nome |should| equal_to("Daniel")
        imovel.proprietario_antigo |should| equal_to("IMOR Tal")

    


if __name__ == "__main__":
    unittest.main()
