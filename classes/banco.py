#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Banco(object):
    def __init__(self):
        self.imoveis_vendidos = []
        self.imoveis_disponiveis = []
        
    def adicionar_imovel_vendido(self,imovel):
        self.imoveis_vendidos.append(imovel)
        
            
