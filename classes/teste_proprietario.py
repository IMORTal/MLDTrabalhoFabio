#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from proprietario import Proprietario
from imoveis import Imovel

class TesteProprietario(unittest.TestCase):

    def setUp(self):
        Proprietario.proprietarios = []

    def teste_criar_proprietario(self):
        self.p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        self.p.nome |should| equal_to("Daniel")
        self.p.cpf |should| equal_to("130.978.257-11")
        self.p.endereco |should| equal_to("Endereco")
        self.p.telefone |should| equal_to("99999999")
        self.p.retornar_proprietarios() |should| have(1).itens #Testando lista "Proprietario.proprietario"

    def teste_retornar_proprietarios(self):
        self.p = Proprietario(nome="Lucas",cpf="cpf",endereco="Endereco",telefone="77777777")
        self.p.retornar_proprietarios() |should| have(1).itens #retorna a lista de todos os proprietarios.
        self.p.retornar_proprietarios()[0].nome |should| equal_to("Lucas")
  

    def teste_comprar_imovel(self):
        self.p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999") #Cadastrando proprietario_antigo
        self.p2 = Proprietario(nome="Carla",cpf="cpf",endereco="Endereco",telefone="22222222") #Cadastrando proprietario_atual        
        self.imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario=self.p) #Cadastrando imovel lista imovel_interesse
        self.p.vender_imovel().bairro |should| equal_to("Centro") #Proprietario vende o imovel pra imobiliaria
        self.imovel.retornar_imoveis_disponiveis() |should| have(1).itens
        self.imovel.retornar_imoveis_disponiveis()[0].bairro |should| equal_to("Centro") 
        imovel_vendido = self.p2.comprar_imovel(self.imovel.retornar_imoveis_disponiveis()[0]) #Proprietario p2(Carla) compra o imovel; Funcao retorna o ultimo imovel da lista Imovel.imovel_vendido 
        imovel_vendido.bairro |should| equal_to("Centro") 
        imovel_vendido.proprietario_atual.nome |should| equal_to("Carla")
        imovel_vendido.proprietario_antigo.nome |should| equal_to("Tereza")
        
    #def teste_retornar_super_vendedores(self): #Retorna proprietários que venderam mais de um imovel para a imobiliária.
     #   self.p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999")
    def teste_vender_imovel(self):
        self.p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999") #Cadastrando proprietario
        self.imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario=self.p) #Cadastrando imovel
        self.p.vender_imovel().bairro |should| equal_to("Centro")
        self.p.vender_imovel().proprietario_atual |should| equal_to("IMOR Tal")
        self.p.vender_imovel().proprietario_antigo.nome |should| equal_to("Tereza")
        

if __name__ == "__main__":
    unittest.main()
