#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Imovel(object):
    #imovel_vendido, imovel_disponivel e imovel_interesse são listas para guardar todas as instâncias da classe Imovel.    

    imovel_vendido = []
    imovel_disponivel = []
    imovel_interesse = []
    
    def __init__(self,endereco,bairro,area,descricao,proprietario):
        self.endereco = endereco
        self.bairro = bairro
        self.area = area
        self.descricao = descricao
        self.proprietario_antigo = ""
        self.proprietario_atual = proprietario
        Imovel.adicionar_imoveis_interesse(self)
        
    
    def retornar_imoveis_vendidos(self):
        return Imovel.imovel_vendido
    
    def retornar_imoveis_disponiveis(self):
        return Imovel.imovel_disponivel

    def retornar_imoveis_interesse(self):
        return Imovel.imovel_interesse

    @staticmethod
    def adicionar_imoveis_vendidos(imovelvendido):
        Imovel.imovel_vendido.append(imovelvendido)
    
    @staticmethod
    def adicionar_imoveis_disponiveis(imoveldisponivel):
        Imovel.imovel_disponivel.append(imoveldisponivel)

    @staticmethod
    def adicionar_imoveis_interesse(imovelinteresse):
        Imovel.imovel_interesse.append(imovelinteresse)

