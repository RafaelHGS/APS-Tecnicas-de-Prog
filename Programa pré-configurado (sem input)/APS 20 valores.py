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

#Cédula 1
from random import seed
from random import randint
import time
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.setrecursionlimit(10 ** 9)


#Cédula 2: Solução Iterativa - QuickSort
def partition(colecao, l, h):
    i = ( l - 1 )
    x = colecao[h]
 
    for j in range(l, h):
        if   colecao[j] <= x:

            i = i + 1
            colecao[i], colecao[j] = colecao[j], colecao[i]
 
    colecao[i + 1], colecao[h] = colecao[h], colecao[i + 1]
    return (i + 1)
 
def quickSortIterative(colecao, l, h): 
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    while top >= 0:
 
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        p = partition( colecao, l, h )
 
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


#Cédula 3: Solução Recursiva - QuickSort
def partition2(colecao, low, high):
    i = (low - 1)        
    pivot = colecao[high]    
 
    for j in range(low, high):
        if colecao[j] <= pivot:
            i += 1
            colecao[i], colecao[j] = colecao[j], colecao[i]
 
    colecao[i + 1], colecao[high] = colecao[high], colecao[i + 1]
    return (i + 1)
 
def quickSortRecursive(colecao, low, high):
    if low < high:
 
        pi = partition2(colecao, low, high)
 
        quickSortRecursive(colecao, low, pi-1)
        quickSortRecursive(colecao, pi + 1, high)

    ## Fim Solução Recursiva


#Cédula 4: Criando Coleção, Utilizando valores aleatórios
def criarColecao(colecao, tamanho):
    for indice in range(0, tamanho):
        valor = np.int64(randint(0, 51))
        colecao.append(valor)


#Cédula Auxiliar do Pandas
def planilha_E_Grafico(tamanho, tIterativa, tRecursiva):

    dadosRegistrados = {"QTD de Nº": tamanho, "T_Solução Recursiva": tRecursiva,
    "T_SoluçãoIterativa": tIterativa,}

    planilha = pd.DataFrame.from_dict(dadosRegistrados)
    planilha.to_excel("Tempos de Soluções.xlsx")

    plt.plot(planilha["T_Solução Recursiva"], planilha["QTD de Nº"], color = "red")
    plt.plot(planilha["T_SoluçãoIterativa"], planilha["QTD de Nº"], color = "blue")

    plt.title("Tempo de Solução - Iterativa x Recursiva")
    plt.xlabel("Tempo em Segundos")
    plt.ylabel("Quantidade Números da Lista/vetor (N)")

    plt.savefig("Grafico - Tempo das Soluções.png")
    plt.show()


#Cédula 5- Função Principal
def main():
    listaDeTamanhos = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000,
    60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
    TAMANHO = 0
    colecao = []

    listaQtdNumeros = []
    tempos_S_Iterativa = []
    tempos_S_Recursiva = []

    repeticoes = 0
    print()
        
    while repeticoes != len(listaDeTamanhos):

        TAMANHO = listaDeTamanhos[repeticoes]

        listaQtdNumeros.append(TAMANHO)

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

        repeticoes +=1

    planilha_E_Grafico(listaQtdNumeros, tempos_S_Iterativa, tempos_S_Recursiva,)

if __name__ == '__main__' :
    main()