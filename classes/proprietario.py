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
        return Imovel.imovel_vendido
        
        
            
   
   
    #O StaticMethod atribui métodos a classe e não a sua instância. Sendo assim:
    #p = Proprietario(<passagem_de_argumentos>)
    #p.adicionar_proprietario(proprietario) | retornaria: NoAtributeError

    @staticmethod
    def adicionar_proprietario(proprietario):
        Proprietario.proprietarios.append(proprietario)
    
        
