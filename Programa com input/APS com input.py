"""
    -Arquivo Base Para Realização da APS, fornecido pelo professor André Santana, através da Plataforma Google Colab

Instituição: Universidade Anhembi Morumbi, Paulista 1
Ano: 2021
Curso: Ciência da Computação
Nome do Aluno: Rafael Henrique Gonçalves Soares
RA: 21566288

Proposta do Programa:
    -O que fazer na APS?

    1- Estudar algoritmo QuickSort
    2- Definir um conjunto de "tamanhos" de experimento para os testes
    3- Rodar os Testes e anotar os tempos
    4- Preparar uma conclusão a respeito do tempo de solução e o custo benefícios para implementação
    5- Apresentar os tempos no formato de tabela
    6- Desafio: Utilizar Pandas e MatplotLib para apresentar os resultados. 0,5 na N2
"""

from Modulos.Funções import quickSortIterative, quickSortRecursive, criarColecao
from Modulos.Pandas_e_Matplotlib import planilha_E_Grafico
import time


#Cédula 5- Função Principal
def main():
    TAMANHO = 0 
    colecao = []

    listaQtdNumeros = []
    tempos_S_Iterativa = []
    tempos_S_Recursiva = []
    repeticoes = 0

    print()

    while repeticoes != 20:
        try:
            TAMANHO = int(input("Digite um número que será o tamanho da lista/vetor: "))
            listaQtdNumeros.append(TAMANHO)
        except:
            print("Digite um número válido !")
            continue

        criarColecao(colecao,  TAMANHO)

        colecaoRecursiva = colecao.copy()
        colecaoIterativa = colecao.copy()

        tempoInicial = time.time() 
        quickSortRecursive(colecaoRecursiva, 0, TAMANHO - 1)
        tempoFinal = time.time()

        tempoTotal = tempoFinal-tempoInicial
        tempos_S_Recursiva.append(tempoTotal)

        print("Tempo Solução Recursiva: {} s".format(tempoFinal - tempoInicial))

        tempoInicial = time.time() 
        quickSortIterative(colecaoIterativa, 0, TAMANHO - 1) 
        tempoFinal = time.time()

        tempoTotal = tempoFinal-tempoInicial
        tempos_S_Iterativa.append(tempoTotal)

        print("Tempo Solução Iterativa: {} s".format(tempoFinal - tempoInicial))
        print()

        repeticoes += 1

    planilha_E_Grafico(listaQtdNumeros, tempos_S_Iterativa, tempos_S_Recursiva)

if __name__ == '__main__' :
    main()

