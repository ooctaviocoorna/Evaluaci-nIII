'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Interpreter

Este ejemplo ayuda al usuario a determinar la calificación del alumnado por medio del
sistema americano de calificación, donde A=10, B=9, C=8, D=7 y E<6
'''

from abc import ABC, abstractmethod

'''AbstractExpression'''
class CalifConver(ABC):
    @abstractmethod
    def interpret(self):
        pass
    
'''NonTerminalExpresions'''
class CalifA(CalifConver):
    def a(self):
        print('El alumno ha obtenido una A de calificación final')
    def interpret(self):
        print('La califiación final del alumno es 10.')

class CalifB(CalifConver):
    def b(self):
         print('El alumno ha obtenido una B de calificación final')
    def interpret(self):
        print('La califiación final del alumno es 9.')

class CalifC(CalifConver):
    def c(self):
         print('El alumno ha obtenido una C de calificación final')
    def interpret(self):
        print('La califiación final del alumno es 8.')

class CalifD(CalifConver):
    def d(self):
         print('El alumno ha obtenido una D de calificación final')
    def interpret(self):
        print('La califiación final del alumno es 7.')

class CalifE(CalifConver):
    def e(self):
         print('El alumno ha obtenido una E de calificación final')
    def interpret(self):
        print('La califiación final del alumno es menor a 6.')

'''Client'''
class CalificacionesFinales:
    def __init__(self):
        self.Sofia=CalifA()
        self.Mario=CalifB()
        self.Ramon=CalifD()
        self.Sofia.a()
        self.Sofia.interpret()
        self.Mario.b()
        self.Mario.interpret()
        self.Ramon.d()
        self.Ramon.interpret()
        
Entrega=CalificacionesFinales()
