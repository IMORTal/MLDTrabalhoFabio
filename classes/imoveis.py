#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Imoveis(object):
    def __init__(self,endereco,bairro,area,descricao,proprietario_atual):
        self.endereco = endereco
        self.bairro = bairro
        self.area = area
        self.descricao = descricao
        self.proprietario_antigo = "IMOR Tal"
        self.proprietario_atual = proprietario_atual       
    

class ImovelVendido(Imoveis):   
    pass   


class ImovelDisponivel(Imoveis):
    pass
