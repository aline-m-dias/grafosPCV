
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
'''
def cost(cost_mat, route):
   return cost_mat[np.roll(route, 1), route].sum() #np.roll gira a rota em uma posição para torná-la facil de usar
                                                   #route para indexar na matriz de custo
                                                   #sum() soma os custos do segmento individual para calcular o custo total da rota.
def cost_change(cost_mat, n1, n2, n3, n4):
    return cost_mat[n1][n3] + cost_mat[n2][n4] - cost_mat[n1][n2] - cost_mat[n3][n4]

def two_opt(route, cost_mat):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                if cost_change(cost_mat, best[i - 1], best[i], best[j - 1], best[j]) < 0:
                    best[i:j] = best[j - 1:i - 1:-1]
                    improved = True
        route = best
    return best


if __name__ == '__main__':
    nodes = 1000
    init_route = list(range(nodes))
    print(init_route)
    cost_mat = np.random.randint(100, size=(nodes, nodes))
    cost_mat += cost_mat.T
    np.fill_diagonal(cost_mat, 0)
    cost_mat = list(cost_mat)
    best_route = two_opt(init_route, cost_mat)
    print(best_route)
'''