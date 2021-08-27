import representacao
import algoritmoPCV

nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
manipulador = open(nome_arquivo, "r")
tempo= int(input("Digite o tempo que deseja executar os algoritmos em segundos:"))
linha = manipulador.readline()  # pega a linha de aresta e vertice
linhaInt = linha.split(' ')
vertice = int(linhaInt[0])
aresta = int(linhaInt[1])
#print(vertice)
#print(aresta)
rep = representacao.representacao_lista(manipulador, vertice, aresta)
rota= algoritmoPCV.vizinhoMaisProximo(rep)
S = algoritmoPCV.twoOpt(rota,rep,tempo)


