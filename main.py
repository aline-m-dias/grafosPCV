import bibiotecaGrafo
import algoritmoPCV
'''import numpy as np'''

nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
manipulador = open(nome_arquivo, 'r')
linha = manipulador.readline()  # pega a linha de aresta e vertice
print(linha)
linhaInt = linha.split(" ")
vertice = int(linhaInt[0])
aresta = int(linhaInt[1])
rep = bibiotecaGrafo.representacao_lista(nome_arquivo,vertice,aresta)
a= algoritmoPCV.vizinhoMaisProximo(rep)