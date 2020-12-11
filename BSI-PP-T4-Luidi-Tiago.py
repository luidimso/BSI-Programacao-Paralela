# -*- coding: utf-8 -*-
#Tiago Corrêa
#Luidi Matheus

from threading import Thread, Lock, Condition
sem = Condition(Lock())

matriz = [[1, 0, 0, 0],  
          [0.6, 1, 0, 0],  
          [0.2, -3, 1, 0],
          [1, 1, 1, 1]]

vetor = [0,0,0,0]
vetorResultado = [1,-7, -26, 4]

somatorio_resultado = 0
index = 0

def somatorio():
    global index
    global somatorio_resultado
    global vetor
    while index < 4:
        count = 0
        if index != 0:
            sem.acquire()
            sem.wait(1)
            sem.release()
            for i in range(index, 0, -1):
                if index < 4:
                    count += matriz[index][i-1]*vetor[i-1]
        else:
            sem.acquire()
            sem.wait(1)
            sem.release()
        somatorio_resultado = count
    
def calc():
    global index
    global somatorio_resultado
    global vetor
    while index < 4:
        sem.acquire()
        sem.wait(3)
        sem.release()
        resultado = (vetorResultado[index]-somatorio_resultado)/matriz[index][index]
        vetor[index] = resultado
        print(vetor)
        index += 1
        
    
t1 = Thread(target = somatorio)
t2 = Thread(target = calc)

t1.start()
t2.start()
t1.join()
t2.join()
