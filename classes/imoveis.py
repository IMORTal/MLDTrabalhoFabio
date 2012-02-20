#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Imovel(object):
    #imovel_vendido e imovel_disponivel são listas para guardar todas as instâncias da classe Imovel.    

    imovel_vendido = []
    imovel_disponivel = []
    
    def __init__(self,endereco,bairro,area,descricao,proprietario):
        self.endereco = endereco
        self.bairro = bairro
        self.area = area
        self.descricao = descricao
        self.proprietario_antigo = proprietario
        self.proprietario_atual = "IMOR-Tal"
        Imovel.adicionar_imoveis_disponiveis(self)
        
    
    def retornar_imoveis_vendidos(self):
        return Imovel.imovel_vendido
    
    def retornar_imoveis_disponiveis(self):
        return Imovel.imovel_disponivel

    @staticmethod
    def adicionar_imoveis_vendidos(imovelvendido):
        Imovel.imovel_vendido.append(imovelvendido)
    
    @staticmethod
    def adicionar_imoveis_disponiveis(imoveldisponivel):
        Imovel.imovel_disponivel.append(imoveldisponivel)

    
