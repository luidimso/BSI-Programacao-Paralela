# -*- coding: utf-8 -*-
#Luidi Matheus
#Tiago Corrêa

import time
from threading import Thread
from random import randint
import threading
Semaphore = threading.Semaphore()

numeroA = 0
numeroB = 0
loopQuantity = 0
timeSleeping = 0


class Trabalho3(Thread):
    def __init__ (self, operation, timeSleeping, semaphore, loopQuantity):
        Thread.__init__(self)
        self.operation = operation
        self.time = timeSleeping
        self.sem = semaphore
        self.loopQuantity = loopQuantity

    def run(self):
        print("Thread da operacao {operation} iniciada.".format(operation = self.operation))
        for x in range(self.loopQuantity):
            if self.operation == "+":
                self.sem.acquire()
                time.sleep(self.time)
                print("Opa, thread de soma acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA + numeroB))
                self.sem.release()
            elif self.operation == "-":
                    self.sem.acquire()
                    time.sleep(self.time)
                    print("Opa, thread de subtração acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA - numeroB))
                    self.sem.release()
            elif self.operation == "*":
                    self.sem.acquire()
                    time.sleep(self.time)
                    print("Opa, thread de multiplicação acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA * numeroB))
                    self.sem.release()
            else:
                self.sem.acquire()
                time.sleep(self.time)
                print("Opa, thread de divisão acabou após {time} segundos. O resultado é {result}".format(time=self.time, result=numeroA / numeroB))
                self.sem.release()

while numeroA == 0:
    print("Informe o primeiro número?")
    numeroA = int(input())

while numeroB == 0:
    print("Informe o segundo número?")
    numeroB = int(input())

while loopQuantity == 0:
    print("Qual é a quantidade de loops?")
    loopQuantity = int(input())

timeSleeping = randint(1, 10)
print("Thread de soma vai ter um ciclo de {time} segundos".format(time=timeSleeping))
threadSoma = Trabalho3("+", timeSleeping, Semaphore, loopQuantity)

timeSleeping = randint(1, 10)
print("Thread de subtração vai ter um ciclo de {time} segundos".format(time=timeSleeping))
threadSubtracao = Trabalho3("-", timeSleeping, Semaphore, loopQuantity)

timeSleeping = randint(1, 10)
print("Thread de multiplicação vai ter um ciclo de {time} segundos".format(time=timeSleeping))
threadMultiplicacao = Trabalho3("*", timeSleeping, Semaphore, loopQuantity)

timeSleeping = randint(1, 10)
print("Thread de divisão vai ter um ciclo de {time} segundos".format(time=timeSleeping))
threadDivisao = Trabalho3("/", timeSleeping, Semaphore, loopQuantity)


threadSoma.start()
threadSubtracao.start()
threadMultiplicacao.start()
threadDivisao.start()
