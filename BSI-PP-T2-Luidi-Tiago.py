# -*- coding: utf-8 -*-
#Luidi Matheus
#Tiago Corrêa

import time
from threading import Thread
from random import randint

numeroA = 0
numeroB = 0
timeSleeping = 0

class Trabalho2(Thread):
    def __init__ (self, operation, timeSleeping):
        Thread.__init__(self)
        self.operation = operation
        self.time = timeSleeping

    def run(self):
        if self.operation == "+":
            time.sleep(self.time)
            print("Opa, thread de soma acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA + numeroB))
        elif self.operation == "-":
            time.sleep(self.time)
            print("Opa, thread de subtração acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA - numeroB))
        elif self.operation == "*":
            time.sleep(self.time)
            print("Opa, thread de multiplicação acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA * numeroB))
        else:
            time.sleep(self.time)
            print("Opa, thread de divisão acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA / numeroB))

while numeroA == 0:
    print("Informe o primeiro número?")
    numeroA = int(input())

while numeroB == 0:
    print("Informe o segundo número?")
    numeroB = int(input())


timeSleeping = randint(1, 20)
print("Thread de soma vai dormir por {time} segundos".format(time=timeSleeping))
threadSoma = Trabalho2("+", timeSleeping)
threadSoma.start()

timeSleeping = randint(1, 20)
print("Thread de subtração vai dormir por {time} segundos".format(time=timeSleeping))
threadSubtracao = Trabalho2("-", timeSleeping)
threadSubtracao.start()

timeSleeping = randint(1, 20)
print("Thread de multiplicação vai dormir por {time} segundos".format(time=timeSleeping))
threadMultiplicacao = Trabalho2("*", timeSleeping)
threadMultiplicacao.start()

timeSleeping = randint(1, 20)
print("Thread de divisão vai dormir por {time} segundos".format(time=timeSleeping))
threadDivisao = Trabalho2("/", timeSleeping)
threadDivisao.start()

