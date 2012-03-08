#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from proprietario import Proprietario, ProprietarioNaoEncontrado, ImovelNaoEncontrado
from imoveis import Imovel

class TesteProprietario(unittest.TestCase):

    def setUp(self):
        Proprietario.proprietarios = []
        Imovel.imovel_disponivel = []
        Imovel.imovel_vendido = []
        Imovel.imovel_interesse = []

    def teste_criar_proprietario(self):
        p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        p.nome |should| equal_to("Daniel")
        p.cpf |should| equal_to("130.978.257-11")
        p.endereco |should| equal_to("Endereco")
        p.telefone |should| equal_to("99999999")
        p.retornar_proprietarios() |should| have(1).itens #Testando lista "Proprietario.proprietarios"

    def teste_retornar_proprietarios(self):
        p = Proprietario(nome="Lucas",cpf="cpf",endereco="Endereco",telefone="77777777")
        p.retornar_proprietarios() |should| have(1).itens #retorna a lista de todos os proprietarios.
        p.retornar_proprietarios()[0].nome |should| equal_to("Lucas")
  

    def teste_comprar_imovel(self):
        p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999") #Cadastrando proprietario_antigo
        p2 = Proprietario(nome="Carla",cpf="cpf",endereco="Endereco",telefone="22222222") #Cadastrando proprietario_atual        
        imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario=p) #Cadastrando imovel lista imovel_interesse
        p.vender_imovel("28 de Março").bairro |should| equal_to("Centro") #Proprietario vende o imovel pra imobiliaria
        imovel.retornar_imoveis_disponiveis() |should| have(1).itens
        imovel.retornar_imoveis_disponiveis()[0].bairro |should| equal_to("Centro") 
        imovel_vendido = p2.comprar_imovel(imovel.retornar_imoveis_disponiveis()[0]) #Proprietario p2(Carla) compra o imovel; Funcao retorna o ultimo imovel da lista Imovel.imovel_vendido
        Imovel.imovel_disponivel |should| have(0).itens 
        Imovel.imovel_vendido |should| have(1).itens
        imovel_vendido.bairro |should| equal_to("Centro") 
        imovel_vendido.proprietario_atual.nome |should| equal_to("Carla")
        imovel_vendido.proprietario_antigo.nome |should| equal_to("Tereza")
        
    
    def teste_vender_imovel(self):
        p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999") #Cadastrando proprietario
        (p.vender_imovel,"28 de Março") |should| throw(ImovelNaoEncontrado)
        imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario=p) #Cadastrando imovel
        Imovel.imovel_interesse |should| have(1).itens
        imovel_vendido = p.vender_imovel("28 de Março")
        imovel_vendido.bairro |should| equal_to("Centro")
        Imovel.imovel_interesse |should| have(0).itens
        Imovel.imovel_disponivel |should| have(1).itens
        imovel_vendido.proprietario_antigo.nome |should| equal_to("Tereza")
        imovel_vendido.proprietario_atual |should| equal_to("IMOR Tal")
    
    def teste_retornar_super_vendedores(self): #Retorna proprietários que venderam mais de um imovel para a imobiliária.
        p = Proprietario(nome="Tereza",cpf="321.422.032-13",endereco="Endereco",telefone="99999999")
        p.retornar_super_vendedores |should| throw(ProprietarioNaoEncontrado)
        imovel = Imovel(endereco="28 de Março",bairro="Centro",area=700.0,descricao="Casa",proprietario=p) #Cadastrando primeiro imovel
        imovel2 = Imovel(endereco="Pelinca",bairro="Centro",area=1200.0,descricao="Casa",proprietario=p)   #Cadastrando segundo imovel     
        p.vender_imovel("28 de Março") #Vendendo primerio imovel
        p.vender_imovel("Pelinca")     #Vendendo segundo imovel
        p.retornar_super_vendedores() |should| have(1).itens
        p.retornar_super_vendedores()[0].nome |should| equal_to("Tereza")
        

    def teste_retornar_super_compradores(self):
        p = Proprietario(nome="carlos", cpf="987.994.321-12", endereco="Endereco", telefone="98989898")
        p.retornar_super_compradores |should| throw(ProprietarioNaoEncontrado)        
        imovel = Imovel(endereco="rua 22", bairro="centro", area=800.0, descricao="casa", proprietario=p)
        imovel2 = Imovel(endereco="rua 42", bairro="centro", area=600.0, descricao="casa", proprietario=p)
        p.vender_imovel("rua 22")        
        p.vender_imovel("rua 42")
        Imovel.imovel_disponivel |should| have(2).itens
        Imovel.imovel_disponivel[0].endereco |should| equal_to("rua 22")
        Imovel.imovel_disponivel[1].endereco |should| equal_to("rua 42")
        p2 = Proprietario(nome="lucas", cpf="432.987.665-77", endereco="rua 71", telefone="67654321")
        p2.comprar_imovel(Imovel.imovel_disponivel[0])
        p2.imoveis_comprados |should| equal_to(1)
        p2.comprar_imovel(Imovel.imovel_disponivel[0])
        p2.imoveis_comprados |should| equal_to(2)
        Proprietario.proprietarios |should| have(2).itens
        Proprietario.proprietarios[1].imoveis_comprados |should| equal_to(2)
        imovel.retornar_imoveis_disponiveis() |should| equal_to([])
        p2.retornar_super_compradores() |should| have(1).itens 
        p2.retornar_super_compradores()[0].nome |should| equal_to("lucas")
        
        
if __name__ == "__main__":
    unittest.main()
