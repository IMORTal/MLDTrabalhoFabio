#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from should_dsl import should
from proprietario import Proprietario

class TesteProprietario(unittest.TestCase):
    def teste_criar_proprietario(self):
        self.p = Proprietario(nome="Daniel",cpf="130.978.257-11",endereco="Endereco",telefone="99999999")
        self.p.nome |should| equal_to("Daniel")
        self.p.cpf |should| equal_to("130.978.257-11")
        self.p.endereco |should| equal_to("Endereco")
        self.p.telefone |should| equal_to("99999999")




if __name__ == "__main__":
    unittest.main()
