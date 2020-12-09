# -*- coding: utf-8 -*-
#Tiago Corrêa
#Luidi Matheus

from threading import Semaphore, Thread
sem = Semaphore(2)
      
matriz = [[2, 0, 0],  
          [1, 4, 0],  
          [1, 1, 1]]

vetor = [0,0,0]
vetorResultado = [2,
                  -3,
                  1]

somatorio_resultado = 0
index = 0

def somatorio():
    global index
    while index < 3:
        print("Somando")
        count = 0
        if index != 0:
            for i in range(index, 0, -1):
                count += matriz[index][i-1]*vetor[i-1]
        somatorio_resultado = count
    
def calc():
    global index
    while index < 3:
        print("Calculando")
        resultado = (vetorResultado[index]-somatorio_resultado)/matriz[index][index]
        vetor[index] = resultado
        print(vetor)
        index += 1
        
    
t1 = Thread(target = somatorio)
t2 = Thread(target = calc)

t1.start()
t1.join()
t2.start()
t2.join()
