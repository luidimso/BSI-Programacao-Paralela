# -*- coding: utf-8 -*-
#Tiago Corrêa
#Luidi Matheus
      
matriz = [[2, 0, 0],  
          [1, 4, 0],  
          [1, 1, 1]]

vetor = [0,0,0]
vetorResultado = [2,
                  -3,
                  1]

def somatorio(index):
    count = 0
    if index != 0:
        for i in range(index, 0, -1):
            print(i, index)
            count += matriz[index][i-1]*vetor[i-1]
        
    return count
    
def calc(index):
    resultado = (vetorResultado[index]-somatorio(index))/matriz[index][index]
    vetor[index] = resultado
    print(vetor)
    
calc(0)
calc(1)
calc(2)
