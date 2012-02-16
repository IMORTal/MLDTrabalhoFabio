#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from banco import Banco
from imoveis import ImovelVendido, ImovelDisponivel
from proprietario import Proprietario

class TesteBanco(unittest.TestCase):
    def teste_criar_banco(self):
        banco = Banco()
        banco.imoveis_vendidos |should| equal_to([])
        banco.imoveis_disponiveis |should| equal_to([])
    
    def teste_adicionar_imovel_vendido(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        imovel = ImovelVendido(endereco="Dr. Manoel Landin 247",bairro="Alphaville",area=500.0,descricao="Casa",proprietario_atual=p)
        banco = Banco()
        banco.adicionar_imovel_vendido(imovel)
        banco.imoveis_vendidos[0].bairro |should| equal_to("Alphaville") 
    
    def teste_adicionar_imovel_disponivel(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")        
        imovel = ImovelDisponivel(endereco="Endereco",bairro="Bairro",area=0,descricao="Descricao",proprietario_antigo=p,preco_minimo=30000)
        banco = Banco()
        banco.adicionar_imovel_disponivel(imovel)
        banco.imoveis_disponiveis[0].bairro |should| equal_to("Bairro")
        banco.imoveis_disponiveis[0].proprietario_atual |should| equal_to("IMOR Tal")
        banco.imoveis_disponiveis[0].proprietario_antigo.nome |should| equal_to("Daniel")


if __name__ == "__main__":
    unittest.main()
