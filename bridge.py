'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Bridge

Este ejemplo ayuda al usuario a entender cómo una fabrica de muñecos crea dos modelos
el femenino y masculino, con dos tonalidades de piel, morena y clara.
'''

from abc import ABC, abstractmethod

'''Implementor'''
class Sexo(ABC):
    @abstractmethod
    def sexoMuneco():
        pass

'''ConcreteImplementorA'''
class Femenino(Sexo):
    def sexoMuneco(self):
        print('Creando muñeco femenino')

'''ConcreteImplementorB'''
class Masculino(Sexo):
    def sexoMuneco(self):
        print('Creando muñeco masculino')

'''Abstraction'''
class TonoPiel(ABC):
    def __init__(self,sexo):
        self.sexo=sexo
    @abstractmethod
    def piel(self):
        pass

'''RedefinedAbstractions'''
class Moreno(TonoPiel):
    def __init__(self,sexo):
        super(Moreno,self).__init__(sexo)
    def piel(self):
        print('Creando muñeco de piel morena.')
        self.sexo.sexoMuneco(self)

class Claro(TonoPiel):
    def __init__(self,sexo):
        super(Claro,self).__init__(sexo)
    def piel(self):
        print('Creando muñeco de piel clara.')
        self.sexo.sexoMuneco(self)
            

class main():
    ninoClaro=Claro(Masculino)
    ninoClaro.piel()
    ninaMorena=Moreno(Femenino)
    ninaMorena.piel()
