#algoritmo construtivo
def vizinhoMaisProximo (grafo):
    U = 0
    C = []
    Q = [ v for v in range (len (grafo)) ] #vertices a visitar
    Q.remove(U) #remove o vértice u
    C.append(U)
    while len(Q) != 0:
        distancia= float('inf')
        for aresta in grafo(U):
            vertice = aresta[0]
            peso = aresta[1]
            if peso <= distancia and vertice in Q: # se o peso da aresta for menor que distancia e o vertice pertencer a Q
                distancia= peso
                V= vertice #adjacente de menor distancia
        C.append(V)
        Q.remove(V)
        U = V
        C.append(C[0])
    print(C)
    return C

#algoritmo de refinamento

