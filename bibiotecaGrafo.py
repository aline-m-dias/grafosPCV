def representacao(arquivo, vertices, arestas, opcao):
    listaAd = [[] for i in range(vertices)]  # cria lista
    matrizAd = [[0 for i in range(vertices)] for i in range(vertices)]  # cria matriz
    for i in range(arestas):
        l = arquivo.readline()
        lInt =l.split(' ')
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = int(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))
        matrizAd[origem][destino] = peso
        matrizAd[destino][origem] = peso
    if opcao == 1:
        return listaAd
    if opcao == 2:
        return matrizAd

    return -1
def representacao_lista(arquivo,vertices,arestas):
    listaAd = [[] for i in range(vertices)]  # cria lista
    for i in range(arestas):
        l = arquivo.readline()
        lInt =l.split(' ')
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = int(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))

    return listaAd

def representacao_matriz(arquivo,vertices,arestas):
    matrizAd = [[0 for i in range(vertices)] for i in range(vertices)]  # cria matriz
    for i in range(arestas):
        l = arquivo.readline()
        lInt = l.split(' ')
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = int(lInt[2])
        matrizAd[origem][destino] = peso
        matrizAd[destino][origem] = peso

    return matrizAd
def informacoesListaAdjacencia(listaad, arestas, vertices):
    maior = 0
    menor = 0
    maiorVertice = -1
    menorVertice = -1
    grau = []
    for i in range(len(listaad)):
        cont = len(listaad[i])
        grau.append(cont)
        if cont > maior:
            maior = cont
            maiorVertice = i
        if cont < maior:
            if menorVertice < cont:
                menor = cont
                menorVertice = i

    grauMedio = (arestas * 2) / vertices
    contMaior = 0
    contMenor = 0
    for i in range(len(grau)):
        if grau[i] == maior:
            contMaior = contMaior + 1
        if grau[i] == menor:
            contMenor = contMenor + 1

    print("-"*30)
    print("Maior grau: {} -  vertice: {}".format(maior, maiorVertice))
    print("Menor grau: {} -  vertice: {}".format(menor, menorVertice))
    print("Grau Médio: {}".format(grauMedio))
    print("Frequecia Relativa: ")
    print("Grau {} :  {} ".format(menor,contMenor/vertices))
    print("Grau {} :  {}".format(maior,contMaior/vertices))
    print("-" * 30)

def informacoesMatrizAdjacencia(matriz, arestas, vertices):
    maior = 0
    menor = 0
    maiorVertice = -1
    menorVertice = -1
    grau = []
    for i in range(vertices):
        cont = vertices - matriz[i].count(0)
        grau.append(cont)
        if cont > maior:
            maior = cont
            maiorVertice = i
        if cont < maior:
            if menorVertice < cont:
                menor = cont
                menorVertice = i

    grauMedio = (arestas * 2) / vertices
    contMaior = 0
    contMenor = 0
    for i in range(len(grau)):
        if grau[i] == maior:
            contMaior = contMaior + 1
        if grau[i] == menor:
            contMenor = contMenor + 1

    print("-" * 30)
    print("Maior grau: {} -  vertice: {}".format(maior, maiorVertice))
    print("Menor grau: {} -  vertice: {}".format(menor, menorVertice))
    print("Grau Médio: {}".format(grauMedio))
    print("Frequecia Relativa: ")
    print("Grau {} :  {} ".format(menor, contMenor / vertices))
    print("Grau {} :  {}".format(maior, contMaior / vertices))
    print("-" * 30)


def buscaLarguralista(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for e in G[u]:
            v = e[0]
            if desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = 1
                nivel[v] = nivel[u] + 1

    contNivel=0
    #print("-"*30)
    #print("Busca largura: ")
    #print("#vertice:nivel")
    for i in range(len(G)):
        if nivel[i] != []:
            #print("{}:{}".format(i, nivel[i]))
            if nivel [i] > contNivel:
                contNivel=nivel[i]

    #print("-" * 30)
    return contNivel


def buscaLarguraMatriz(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                Q.append(i)
                R.append(i)
                desc[i] = 1
                nivel[i] = nivel[u] + 1
    print("-" * 30)
    print("Busca largura: ")
    print("#vertice:nivel")
    for i in range(len(G)):
        if nivel[i] != []:
            print("{}:{}".format(i, nivel[i]))
    print("-" * 30)

    return R

def buscaProfundidadeLista(G,s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for e in G[u]:
            v = e[0]
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                nivel[v] = nivel[u] + 1
                break
        if desempilhar:
            S.pop()

    print("-" * 30)
    print("Busca por profundidade:")
    print("#vertice:nivel")
    for i in range(len(G)):
        if (nivel[i] != []):
            print("{}:{}".format(i,nivel[i]))
    print("-" * 30)

    #return R
def buscaProfundidadeMatriz(G,s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                desempilhar = False
                S.append(i)
                R.append(i)
                desc[i] = 1
                nivel[i] = nivel[u] + 1
                break
        if desempilhar:
            S.pop()
    print("-"*30)
    print("Busca por profundidade:")
    for i in range(len(G)):
        if (nivel[i] != []):
            print ("{}:{}".format(i, nivel[i]))
    print("-"*30)
    #return R

def buscaProfundidadeListaConexa(G, s, marca):
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    vComp[s]=marca
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for e in G[u]:
            v = e[0]
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break
        vComp[u]=marca
        if desempilhar:
            S.pop()


def componentesConexasLista(G):
    global vComp
    vComp = [0 for i in range(len(G))]
    marca = 0
    for i in range(len(G)):
        if vComp[i] == 0:
            marca= marca + 1
            buscaProfundidadeListaConexa(G, i, marca)


    print("Componentes Conexas:{}".format(marca))
    n = max(vComp)
    for i in range(1,n+1):
        print("{} vertices".format(vComp.count(i)))

def buscaProfundidadeConexaMatriz(G, s, marca):
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    vComp[s]=marca
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                desempilhar = False
                S.append(i)
                R.append(i)
                desc[i] = 1
                break
        vComp[u]=marca
        if desempilhar:
            S.pop()

def componentesConexasMatriz(G):
    global vComp
    vComp = [0 for i in range(len(G))]
    marca = 0
    for i in range(len(G)):
        if vComp[i] == 0:
            marca= marca + 1
            buscaProfundidadeConexaMatriz(G,i,marca)

    print("Componentes Conexas:{}".format(marca))
    n = max(vComp)
    for i in range(1,n+1):
        print("{} vertices".format(vComp.count(i)))