'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: FlyWeight

Este ejemplo ayuda al usuario a conocer el modo en la que se crean las playeras de un equipo
de futbol para cada uno de sus jugadores, donde cada una comporten colores y logos, pero
se diferencían por el nombre y el nombre del jugador.
'''
from abc import ABC, abstractmethod

class CamisetasFactory:
    def __init__(self):
        self.camisetas = {}

    def get_camisetas(self, key):
        try:
            camiseta = self.camisetas[key]
        except KeyError:
            camiseta = CrearCamiseta()
            self.camisetas[key] = camiseta
        return camiseta

class Camiseta(ABC):

    def __init__(self):
        self.name = None

    @abstractmethod
    def definirNombre(self, numero):
        pass

class CrearCamiseta(Camiseta):
    
    def definirNombre(self, numero):
        Camiseta.definirNombre(self, numero)

class Client():
    def comprar(self):
        camisetasNuevas = CamisetasFactory()
        concrete_flyweight = camisetasNuevas.get_camisetas("key")
        concrete_flyweight.definirNombre(None)

c = Client()
c.comprar()
