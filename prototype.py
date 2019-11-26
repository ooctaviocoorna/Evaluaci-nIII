'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Prototype

Este ejemplo ayuda al usuario al usuario a enteder cómo un mouse puede ser creado de forma
inalambrica y alambrica a partir de un prototipo de mouse.
'''
from abc import ABC, abstractmethod
import copy

_color=None
_marca=None
'''Prototype'''
class PrototipoMouse(ABC):
    def color(self):
        return self._color
    def marca(self):
        return self._marca
    @abstractmethod
    def ClonarMouse(self):
        pass
    
'''ConcretPrototype1'''
class MouseAlambrico(PrototipoMouse):
    def __init__(self):
        self._color='Negro'
        self._marca='HP'
    def ClonarMouse(self):
        #copyA= copy.copy(self)
        print('Mouse Alambrico negro creado')
    
'''ConcretPrototype2'''
class MouseInalambrico(PrototipoMouse):
    def __init__(self):
        self._color='Rosa'
        self._marca='HP'
    def ClonarMouse(self):
        #copyB= copy.copy(self)
        print('Mouse Inalambrico rosa creado')

class CrearMouse():
    def __init__(self):
        self.MouseAlambricoNegro=MouseAlambrico()
        self.MouseInalambricoRosa=MouseInalambrico()
        self.MouseAlambricoNegro.ClonarMouse()
        self.MouseInalambricoRosa.ClonarMouse()

creacion=CrearMouse()
