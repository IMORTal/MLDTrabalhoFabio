#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from proprietario import Proprietario
from imoveis import Imovel

class TesteProprietario(unittest.TestCase):

    def teste_criar_proprietario(self):
        self.p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        self.p.nome |should| equal_to("Daniel")
        self.p.cpf |should| equal_to("130.978.257-11")
        self.p.endereco |should| equal_to("Endereco")
        self.p.telefone |should| equal_to("99999999")
        self.p.retornar_proprietarios() |should| have(3).itens #Testando lista "Proprietario.proprietario" contem 3 itens nessa parte do teste - ENTENDI NADA

    def teste_retornar_proprietarios(self):
        self.p = Proprietario(nome="Lucas",cpf="cpf",endereco="Endereco",telefone="77777777")
        self.p.retornar_proprietarios() |should| have(4).itens #Lista "Proprietario.proprietario" contem 4 itens - Não entendi direito o porquê.
        self.p.retornar_proprietarios()[0].nome |should| equal_to("Tereza")
        self.p.retornar_proprietarios()[1].nome |should| equal_to("Carla")
        self.p.retornar_proprietarios()[2].nome |should| equal_to("Daniel")
        self.p.retornar_proprietarios()[3].nome |should| equal_to("Lucas")

    def teste_comprar_imovel(self):
        self.p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999") #Cadastrando proprietario_antigo
        self.p2 = Proprietario(nome="Carla",cpf="cpf",endereco="Endereco",telefone="22222222") #Cadastrando proprietario_atual        
        self.imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario=self.p) #Cadastrando imovel
        imovel_disponivel = self.imovel.retornar_imoveis_disponiveis()
        imovel_disponivel |should| have(1).itens
        imovel_disponivel[0].bairro |should| equal_to("Centro") 
        imovel_vendido = self.p2.comprar_imovel(imovel_disponivel[0]) #Proprietario p2(Carla) compra o imovel; Funcao retorna lista Imovel.imovel_vendido 
        imovel_vendido[len(imovel_vendido)-1].bairro |should| equal_to("Centro") 
        imovel_vendido[len(imovel_vendido)-1].proprietario_atual.nome |should| equal_to("Carla")
        imovel_vendido[len(imovel_vendido)-1].proprietario_antigo.nome |should| equal_to("Tereza")
        
        

if __name__ == "__main__":
    unittest.main()
