#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from imoveis import Imoveis, ImovelVendido


class TesteImoveis(unittest.TestCase):
    def teste_criar_imovel(self):
        imovel = Imoveis(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_antigo="Nilton",preco_minimo=120000)
        imovel.endereco |should| equal_to("Dr. Manoel Landin 247")
        imovel.bairro |should| equal_to("Alphaville")
        imovel.descricao |should| equal_to("Casa")
        imovel.area |should| equal_to(500.0)
        imovel.proprietario_antigo |should| equal_to("Nilton")
        imovel.proprietario_atual |should| equal_to("IMOR Tal")
        imovel.preco_minimo |should| equal_to(120000)

class TesteImovelVendido(unittest.TestCase):

    def teste_criar_imovel_vendido(self):
        imovel = ImovelVendido(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_antigo="Nilton",preco_minimo=120000)
        imovel.endereco |should| equal_to("Dr. Manoel Landin 247")
        imovel.bairro |should| equal_to("Alphaville")
        imovel.descricao |should| equal_to("Casa")
        imovel.area |should| equal_to(500.0)
        imovel.proprietario_antigo |should| equal_to("Nilton")
        imovel.proprietario_atual |should| equal_to("IMOR Tal")
        imovel.preco_minimo |should| equal_to(120000)


if __name__ == "__main__":
    unittest.main()
