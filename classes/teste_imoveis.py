#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from imoveis import Imovel
from proprietario import Proprietario


class TesteImoveis(unittest.TestCase):
    def teste_criar_imovel(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        imovel = Imovel(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_atual=p,estado="Disponivel")
        imovel.endereco |should| equal_to("Dr. Manoel Landin 247")
        imovel.bairro |should| equal_to("Alphaville")
        imovel.descricao |should| equal_to("Casa")
        imovel.area |should| equal_to(500.0)
        imovel.proprietario_atual.nome |should| equal_to("Daniel")
        imove.retornar_imoveis_disponiveis() |should| equal_to(1)

    def teste_retornar_imoveis_vendidos(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")        
        imovel = Imovel(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_atual=p,estado="Vendidos")
        imovel.retornar_imoveis_vendidos() |should| have(1).itens             
        imovel.retornar_imoveis_vendidos()[0].bairro |should| equal_to("Alphaville")
        imovel.retornar_imoveis_vendidos()[0].endereco |should| equal_to("Dr. Manoel Landin 247")
        imovel.retornar_imoveis_vendidos()[0].area |should| equal_to(500.0)
        imovel.retornar_imoveis_vendidos()[0].descricao |should| equal_to("Casa")
        imovel.retornar_imoveis_vendidos()[0].proprietario_atual.nome |should| equal_to("Daniel")

    def teste_retornar_imoveis_disponiveis(self):
        p = Proprietario(nome="Maickon",cpf="321.422.032-13",endereco="Endereco",telefone="99999999")        
        imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario_atual=p,estado="Disponivel")
        imovel.retornar_imoveis_disponiveis() |should| have(2).itens             
        imovel.retornar_imoveis_disponiveis()[1].bairro |should| equal_to("Centro")
        imovel.retornar_imoveis_disponiveis()[1].endereco |should| equal_to("28 de Março")
        imovel.retornar_imoveis_disponiveis()[1].area |should| equal_to(500.0)
        imovel.retornar_imoveis_disponiveis()[1].descricao |should| equal_to("Casa")
        imovel.retornar_imoveis_disponiveis()[1].proprietario_atual.nome |should| equal_to("Maickon")


if __name__ == "__main__":
    unittest.main()
