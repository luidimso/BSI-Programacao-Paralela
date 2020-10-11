#Luidi Matheus
#Tiago Corrêa

from threading import Thread

TEXTOS = ["Programacao Paralela", "Instituto Federal Fluminense"]

class Trabalho1(Thread):
    def __init__ (self, index):
        Thread.__init__(self)
        self.index = index

    def run(self):
        print(TEXTOS[self.index])

for texto_index in range (2):
    thread = Trabalho1(texto_index)
    thread.start()