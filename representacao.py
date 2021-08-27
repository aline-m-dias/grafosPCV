def representacao_lista(arquivo,vertices,arestas):
    listaAd = [[] for i in range(vertices)]  # cria lista
    for i in range(arestas):
        l = arquivo.readline()
        lInt = l.split(' ')
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = float(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))

    return listaAd