'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Builder

Este ejemplo ayuda al usuario a saber cómo se crea en una cerámica, las piezas de un
nacimiento de 6 piezas de barro según su molde.
'''
from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Moldes(ABC):
    @abstractproperty
    def nino(self) -> None:
        pass
    @abstractmethod
    def maria(self) -> None:
        pass
    @abstractmethod
    def jose(self) -> None:
        pass
    @abstractmethod
    def reyFlaco(self) -> None:
        pass
    @abstractmethod
    def reyBola(self) -> None:
        pass
    @abstractmethod
    def reyChaparro(self) -> None:
        pass
    
    
class PiezasNacimiento(Moldes):
    def __init__(self) -> None:
        self.vaceador()
    def vaceador(self) -> None:
        self._nacimiento = Nacimiento()
    @property
    def nacimiento(self) -> Nacimiento:
        nacimiento = self._nacimiento
        self.vaceador()
        return nacimiento
    def nino(self) -> None:
        self.nacimiento.add("Niño")
    def maria(self) -> None:
        self.nacimiento.add("María")
    def jose(self) -> None:
        self.nacimiento.add("José")
    def reyFlaco(self) -> None:
        self.nacimiento.add("Rey Flaco")
    def reyBola(self) -> None:
        self.nacimiento.add("Rey Bola")
    def reyChaparro(self) -> None:
        self.nacimiento.add("Rey Chaparro")
    

class Nacimiento():
    def __init__(self) -> None:
        self.piezas = []
    def add(self, part: Any) -> None:
        self.piezas.append(part)
    def material(self) -> None:
        print(f"Piezas: {', '.join(self.piezas)}", end="")

class Ceramica:
    def __init__(self) -> None:
        self._vacear = None

    @property
    def vacear(self) -> Moldes:
        return self._vacear

    @vacear.setter
    def vacear(self, vacear: Moldes) -> None:
        self._vacear = vacear

    def piezasListas(self) -> None:
        self.vacear.nino()
        self.vacear.maria()
        self.vacear.jose()
        self.vacear.reyFlaco()
        self.vacear.reyBola()
        self.vacear.reyChaparro()
        
        
if __name__ == "__main__":

    ceramica = Ceramica()
    vacear = PiezasNacimiento()
    ceramica.vacear = vacear

