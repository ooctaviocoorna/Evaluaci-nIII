'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Prototype

Este ejemplo ayuda al usuario al usuario a enteder cómo un mouse puede ser creado de forma
inalambrica y alambrica a partir de un prototipo de mouse.
'''
from abc import ABC, abstractmethod

'''Prototype'''
class PrototipoMouse(ABC):
    color='Negro'
    marca='HP'
    print('PROTOTIPO')
    print('Color: ',color)
    print('Marca: ',marca)
    print(' ')
        
    @abstractmethod
    def ClonarMouse(self):
        pass
    
'''ConcretPrototype1'''
class MouseAlambrico(PrototipoMouse):
    def __init__(self):
        PrototipoMouse.__init__(self)
        print('Creando mouse alambrico.')
        
    def ClonarMouse(self):
        
        print('Color: ',PrototipoMouse.color)
        print('Marca: ',PrototipoMouse.marca)
    
'''ConcretPrototype2'''
class MouseInalambrico(PrototipoMouse):
    def __init__(self):
        PrototipoMouse.__init__(self)
        print('Creando mouse inalambrico.')
        
    def ClonarMouse(self):
        
        print('Color: ',PrototipoMouse.color)
        print('Marca: ',PrototipoMouse.marca)
class CrearMouse():
    def __init__(self):
        self.MouseAlambrico=MouseAlambrico()
        self.MouseAlambrico.ClonarMouse()
        self.MouseInalambrico=MouseInalambrico()
        self.MouseInalambrico.ClonarMouse()
creacion=CrearMouse()
