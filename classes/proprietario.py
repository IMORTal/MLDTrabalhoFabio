#!/usr/bin/env python
#-*- coding:utf-8 -*-

from imoveis import Imovel

class Proprietario(object):
    proprietarios = []    
    def __init__(self,nome,cpf,endereco,telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        Proprietario.adicionar_proprietario(self)

    def retornar_proprietarios(self):
        return Proprietario.proprietarios
 
    def comprar_imovel(self,imovel):
        Imovel.imovel_disponivel.remove(imovel)        
        imovel.proprietario_atual = self
        Imovel.imovel_vendido.append(imovel)
        return Imovel.imovel_vendido[len(Imovel.imovel_vendido)-1]
        
    def vender_imovel(self):
        for imovel in Imovel.imovel_interesse:
            if imovel.proprietario_atual.nome == self.nome:
                imovel_a_vender = imovel
                Imovel.imovel_interesse.remove(imovel_a_vender)
                imovel_a_vender.proprietario_antigo = imovel_a_vender.proprietario_atual
                imovel_a_vender.proprietario_atual = "IMOR Tal"
                Imovel.imovel_disponivel.append(imovel_a_vender)
            else:
                return ("Imovel não encontrado!")
        return Imovel.imovel_disponivel[len(Imovel.imovel_disponivel)-1]
   
   
    #O StaticMethod atribui métodos a classe e não a sua instância. Sendo assim:
    #p = Proprietario(<passagem_de_argumentos>)
    #p.adicionar_proprietario(proprietario) | retornaria: NoAtributeError

    @staticmethod
    def adicionar_proprietario(proprietario):
        Proprietario.proprietarios.append(proprietario)
    
        
