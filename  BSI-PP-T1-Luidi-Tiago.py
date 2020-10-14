#Luidi Matheus
#Tiago Corrêa

from threading import Thread

TEXTOS = ["Programacao Paralela", "Instituto Federal Fluminense"]

##Classe que imprime texto.
class Trabalho1(Thread):
    def __init__ (self, index, input_value):
        Thread.__init__(self)
        self.index = index
        self.value = input_value

    def run(self):
        print(self.value)
##-------------------------

for texto_index in range (2):
    thread = Trabalho1(texto_index, TEXTOS[texto_index])
    thread.start()