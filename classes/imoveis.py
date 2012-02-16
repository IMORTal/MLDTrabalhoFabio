#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Imoveis(object):
    def __init__(self,endereco,bairro,area,descricao,proprietario_antigo,preco_minimo):
        self.endereco = endereco
        self.bairro = bairro
        self.area = area
        self.descricao = descricao
        self.proprietario_antigo = proprietario_antigo
        self.proprietario_atual = "IMOR Tal"        
        self.preco_minimo = preco_minimo
    

class ImovelVendido(Imoveis):   
    def __init__(self,preco_de_venda):
        super
        self.preco_de_venda = preco_de_venda   
