'''
Created on 23 nov. 2019

@author: jcorona

Deisgn Pattern: Interpreter

Este ejemplo ayuda al usuario a determinar la calificación del alumnado por medio del
sistema americano de calificación, donde A=10, B=9, C=8, D=7 y E<6
'''

from abc import ABC, abstractmethod

'''Context'''
class TestInt():
    califE=input('¿Cuál es tu calificación? ')
    def getEntrada(self):
        return califE
    def setEntrada(Self):
        califE = califE

'''AbstractExpression'''
class CalifConver(ABC):
    @abstractmethod
    def interpret(self):
        print('')
    
'''NonTerminalExpresions'''
class CalifAme(CalifConver):
    def a(TestInt):
        if califE=='A':
            print('El alumno ha obtenido una A de calificación final')
            def interpret(self):
                print('La califiación final del alumno es 10.')
    def b(TestInt):
        if califE=='B':
            print('El alumno ha obtenido una B de calificación final')
            def interpret(self):
                print('La califiación final del alumno es 9.')
    def c(TestInt):
        if califE=='C':
            print('El alumno ha obtenido una C de calificación final')
            def interpret(self):
                print('La califiación final del alumno es 8.')
    def d(TestInt):
        if califE=='D':
            print('El alumno ha obtenido una D de calificación final')
            def interpret(self):
                print('La califiación final del alumno es 7.')
    def e(TestInt):
        if califE=='E':
            print('El alumno ha obtenido una E de calificación final')
            def interpret(self):
                print('La califiación final del alumno es 6.')

'''Client'''
class CalificacionesFinales:
    def __init__(self):
        self.Alumno=TestInt()
Entrega=CalificacionesFinales()
