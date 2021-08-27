import random
from time import time

#algoritmo construtivo

def vizinhoMaisProximo (grafo):

    U = 0
    C = []
    Q = [i for i in range(len(grafo))] #vertices a visitar
    C.append(0)
    Q.remove(U)  # remove o vértice u
    while len(Q) != 0:
        distancia= float('inf')
        for aresta in grafo[U]:
                vertice = aresta[0]
                peso = aresta[1]
                if peso <= distancia and vertice in Q:
                    distancia= peso
                    V= vertice #adjacente de menor distancia
        C.append(V)
        Q.remove(V)
        U = V
    C.append(C[0])
    return C

#algoritmo de refinamento
def avaliaCusto(S, grafo):
    custo = 0
    for i in range(len(S)-1):
        u = S[i]
        v = S[i+1]
        for j in grafo[u]:
            if j[0] == v:
                custo = custo + j[1]
                break
    return custo

def twoOpt(S, grafo,tempo):

    inicio = time()

    while time() - inicio < tempo:
        #escolha aleatória das arestas
        aresta1 = random.choice(S)
        #print(aresta1)
        aresta2 = random.choice(S)
        #print(aresta2)

        if aresta1 != S[0] and aresta2 != S[0] and aresta1 != aresta2:

            S1 = S[:] #recebe a rota S

            #verifica a ocorrencia da aresta
            S1[S1.index(aresta1)] = aresta2
            S1[S1.index(aresta2)] = aresta1

            c1 = avaliaCusto(S, grafo)
            c2 = avaliaCusto(S1, grafo)

            if c2 < c1:
                S = S1

    arquivo= open('saida_algoritmo_refinamento.txt', 'w+')
    arquivo.write(("Distancia 2-OPT:{} \n".format(c2)))
    arquivo.write(("Tempo:{} segundos \n".format(time() -inicio)))
    arquivo.write(("Rota 2-OPT:{}\n".format(S)))



    return S

