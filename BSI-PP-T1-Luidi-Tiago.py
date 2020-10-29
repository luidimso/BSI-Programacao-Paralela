# -*- coding: utf-8 -*-
#Luidi Matheus
#Tiago Corrêa

from threading import Thread

TEXTOS = ["Programacao", "Instituto"]

##Classe que imprime texto.
class Trabalho1(Thread):
    def __init__ (self, input_value):
        Thread.__init__(self)
        self.value = input_value

    def run(self):
        print(self.value)
##-------------------------

thread1 = Trabalho1(TEXTOS[0])
thread1.start()
thread2 = Trabalho1(TEXTOS[1])
thread2.start()
