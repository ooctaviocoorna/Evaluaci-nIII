'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Bridge

Este ejemplo ayuda al usuario a entender cómo una fabrica de muñecos crea dos modelos
el femenino con vestido y pelo largo, y el masculino con pantalon y camisa y pelo corto
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

'''Abstraction
class Maquina(ABC):
    @abstractmethod
    def creaNino():
        pass
    def creaNina():
        pass
'''

'''RefinedAbstraction'''
class Creacion:
    def __init__(self):
        self.ninoWero=Masculino()
        self.ninaWera=Femenino()
        self.ninoWero.sexoMuneco()
        self.ninaWera.sexoMuneco()

CrearMunecos=Creacion()
