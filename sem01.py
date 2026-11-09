import multiprocessing
import time
semaforo = None
def init(sema):
    global semaforo
    semaforo = sema
def carro(id, sentido):
    print('Carro', id, 'parado')
    with semaforo:
        print('Carro', id, 'indo para', sentido)
        print('carro', id, 'saiu do cruzamento')
def main():
    parametros = [0]*4
    parametros[0] = (1, 'baixo')
    parametros[1] = (2, 'direita')
    parametros[2] = (3, 'esquerda')
    parametros[3] = (4, 'cima')
    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=4,initializer=init,initargs=(sem,)) as threads:
            threads.starmap(carro, parametros)
if __name__ == '__main__':
    main()