# -*- coding: utf-8 -*-
#Tiago Corrêa
#Luidi Matheus

import threading 
import time 
import random
import sys
sem = threading.Semaphore()

numeroA = 0
numeroB = 0
loopQuantity = 0

#soma
def fun1(a, b, quantidadeLoop): 
    global lock, loopQuantity
    t = 0
    while quantidadeLoop > 0: 
        sem.acquire() 
        print("SOMA = {r}".format(r = a+b))

        if t == 0:
            t = random.randint(1,10)
            print("Gerando tempo de descanco da thread de adicao....{tempo} segundos.".format(tempo = t))

        time.sleep(t) 
        quantidadeLoop-=1
        sem.release() 
        
#subtracao
def fun2(a, b, quantidadeLoop): 
    global lock, loopQuantity
    t = 0
    while quantidadeLoop > 0: 
        sem.acquire()
        print("SUBTRACAO = {r}".format(r = a-b))
        if t == 0:
            t = random.randint(1,10)
            print("Gerando tempo de descanço da thread de subtracao....{tempo} segundos.".format(tempo = t))

        time.sleep(t)
        quantidadeLoop-=1
        sem.release()
#multiplicacao
def fun3(a, b, quantidadeLoop): 
    global lock, loopQuantity
    t = 0
    while quantidadeLoop > 0: 
        sem.acquire()
        print("MULTIPLICACAO = {r}".format(r = a*b))

        if t == 0:
            t = random.randint(1,10)
            print("Gerando tempo de descanço da thread de multiplicacao....{tempo} segundos.".format(tempo = t))

        time.sleep(t)
        quantidadeLoop-=1
        sem.release()
#divisao
def fun4(a, b, quantidadeLoop): 
    global lock, loopQuantity
    t = 0
    while quantidadeLoop > 0: 
        sem.acquire()
        print("DIVISAO = {r}".format(r = a/b))

        if t == 0:
            t = random.randint(1,10)
            print("Gerando tempo de descanço da thread de divisão....{tempo} segundos.".format(tempo = t))

        time.sleep(t)
        quantidadeLoop-=1
        sem.release()


while numeroA == 0:
    print("Informe o primeiro número?")
    numeroA = int(input())

while numeroB == 0:
    print("Informe o segundo número?")
    numeroB = int(input())

while loopQuantity == 0:
    print("Por quantas vezes o algoritimo vai se repetir?")
    loopQuantity = int(input())

print("----------------------------Iniciando threads....")
t1 = threading.Thread(target = fun1, args=(numeroA, numeroB, loopQuantity))
t1.start()

t2 = threading.Thread(target = fun2, args=(numeroA, numeroB, loopQuantity))
t2.start()
t2.join()

t3 = threading.Thread(target = fun3, args=(numeroA, numeroB, loopQuantity))
t3.start()
t3.join()

t4 = threading.Thread(target = fun4, args=(numeroA, numeroB, loopQuantity))
t4.start()
t4.join()
