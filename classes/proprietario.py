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
        self.imoveis_vendidos = 0
        self.imoveis_comprados = 0
        Proprietario.adicionar_proprietario(self)

    def retornar_proprietarios(self):
        return Proprietario.proprietarios
 
    def comprar_imovel(self,imovel):
        self.imoveis_comprados += 1   
        Imovel.imovel_disponivel.remove(imovel)        
        imovel.proprietario_atual = self
        Imovel.imovel_vendido.append(imovel)
        return Imovel.imovel_vendido[len(Imovel.imovel_vendido)-1]
        
    def vender_imovel(self,endereco):
        check = 0
        for imovel in Imovel.imovel_interesse:
            if imovel.proprietario_atual.nome == self.nome and imovel.endereco == endereco:
                check = 1                    
                imovel_a_vender = imovel
                self.imoveis_vendidos += 1
                Imovel.imovel_interesse.remove(imovel_a_vender)
                imovel_a_vender.proprietario_antigo = imovel_a_vender.proprietario_atual
                imovel_a_vender.proprietario_atual = "IMOR Tal"
                Imovel.imovel_disponivel.append(imovel_a_vender)    
        if check == 1:
            return Imovel.imovel_disponivel[len(Imovel.imovel_disponivel)-1]
        else:
            raise ImovelNaoEncontrado ("Imovel não encontrado!")
   
    def retornar_super_vendedores(self):
        check = 0        
        super_vendedores = []
        for proprietario in Proprietario.proprietarios:
            if proprietario.imoveis_vendidos >= 2:
                check = 1
                super_vendedores.append(proprietario)
        if check == 0:
            raise ProprietarioNaoEncontrado("Nenhum super vendedor encontrado")
        else:
            return super_vendedores               


    def retornar_super_compradores(self):
        super_compradores = []
        check = 0
        for proprietario in Proprietario.proprietarios:                
            if proprietario.imoveis_comprados >= 2:
                check = 1
                super_compradores.append(proprietario)   
        if check == 0:
            raise ProprietarioNaoEncontrado("Nenhum super comprador encontrado")
        else:        
            return super_compradores 

    #O StaticMethod atribui métodos a classe e não a sua instância. Sendo assim:
    #p = Proprietario(<passagem_de_argumentos>)
    #p.adicionar_proprietario(proprietario) | retornaria: NoAtributeError

    @staticmethod
    def adicionar_proprietario(proprietario):
        Proprietario.proprietarios.append(proprietario)
    
class ProprietarioNaoEncontrado(Exception):
    pass        

class ImovelNaoEncontrado(Exception):
    pass
