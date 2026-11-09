import multiprocessing
import random
import time
chegada = None
semaforo = None
def init(cheg, sema):
    global chegada
    global semaforo
    chegada = cheg
    semaforo = sema
def sapo(id, dist):
    p = 0
    while p < dist:
        salto = random.randint(1, 5)
        p = p + salto
        print('O sapo', id, 'pulou', salto, 'CMs')
        print('O sapo', id, 'percorreu', p, 'CMs')
        time.sleep(0.3)
    with semaforo:
        chegada.value = chegada.value + 1
        if chegada.value == 1:
            print('Sapo', id, 'venceu')
        else:
            print('Sapo', id, 'chegou em', chegada.value, 'lugar')
def main():
    id: int = 1
    tam: int = 10
    parametros = [0]*5
    for i in range(5):
        parametros[i] = (id, tam)
        id += 1
    chegada = multiprocessing.Value('i', 0)
    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=5,initializer=init,initargs=(chegada, sem)) as threads:
            threads.starmap(sapo, parametros)
if __name__ == '__main__':
    main()