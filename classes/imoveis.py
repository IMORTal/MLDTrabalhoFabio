#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Imovel(object):
    imovel_vendido = []
    imovel_disponivel = []
    def __init__(self,endereco,bairro,area,descricao,proprietario_atual,estado):
        self.endereco = endereco
        self.bairro = bairro
        self.area = area
        self.descricao = descricao
        self.proprietario_antigo = "IMOR Tal"
        self.proprietario_atual = proprietario_atual
        if estado == "Disponivel":
            Imovel.adicionar_imoveis_disponiveis(self)
        else:
            Imovel.adicionar_imoveis_vendidos(self)
    
    
    def retornar_imoveis_vendidos(self):
        return Imovel.imovel_vendido
    
    @staticmethod
    def adicionar_imoveis_vendidos(imovelvendido):
        Imovel.imovel_vendido.append(imovelvendido)
    
    @staticmethod
    def adicionar_imoveis_disponiveis(imoveldisponivel):
        Imovel.imovel_disponivel.append(imoveldisponivel)

    
