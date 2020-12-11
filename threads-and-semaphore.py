import threading
import time
import random

def Semaphore(n,cor,delay, semaphore, lock):
    print("A thread de cor {0} vai esperar {1} segundos para printar".format(cor,delay))    
    for i in range(n):  
        semaphore.acquire()
        time.sleep(delay)
        lock.release()
        print("{0}".format(cor))        

def main():
    n = int(input("Numero de vezes para rodar:"))
    threads = []
    semaphore_red = threading.Semaphore()
    semaphore_green = threading.Semaphore(0)
    semaphore_yellow = threading.Semaphore(0)
    r = random.randint(1, 10)
    threads.append(threading.Thread(target=Semaphore, args=(n,'Amarelo',r,semaphore_yellow, semaphore_green,)))
    r = random.randint(1, 10)
    threads.append(threading.Thread(target=Semaphore, args=(n,'Verde',r,semaphore_green, semaphore_red,)))
    r = random.randint(1, 10)
    threads.append(threading.Thread(target=Semaphore, args=(n, 'Vermelho',r,semaphore_red, semaphore_yellow,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
