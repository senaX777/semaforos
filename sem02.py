import multiprocessing
import random
import time
semaforo = None
def init(sema):
    global semaforo
    semaforo = sema
def pessoa(id):
    vel: int = 0
    t: float = 0.0
    vel = random.randint(4, 6)
    t = 200 / vel
    print('Pessoa', id, 'comecou a andar a', vel, 'ms')
    time.sleep(t)
    print('Pessoa', id, 'chegou a porta')
    with semaforo:
        t = random.randint(1, 2)
        print('Pessoa', id, 'comcou a atravessar a porta')
        time.sleep(t)
        print('Pessoa', id, 'atravessou a porta')
def main():
    parametros = [0]*4
    for i in range(0, 4, 1):
        parametros[i] = i + 1
    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool( processes=4,initializer=init,initargs=(sem,)) as threads:
            threads.map(pessoa, parametros)
if __name__ == '__main__':
    main()