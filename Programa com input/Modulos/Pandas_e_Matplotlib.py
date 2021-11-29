#Cédula Auxiliar
def planilha_E_Grafico(tamanho, tIterativa, tRecursiva):
    import pandas as pd
    import matplotlib.pyplot as plt

    listaQtdNumeros = tamanho

    temposSolucaoIterativa = tIterativa
    temposSolucaoRecursiva = tRecursiva

    dadosRegistrados = {"QTD de Nº": listaQtdNumeros, "T_Solução Recursiva": temposSolucaoRecursiva,
    "T_SoluçãoIterativa": temposSolucaoIterativa}

    planilha = pd.DataFrame.from_dict(dadosRegistrados)
    planilha.to_excel("Tempos de Soluções.xlsx")

    plt.plot(planilha["T_Solução Recursiva"], planilha["QTD de Nº"], color = "red")
    plt.plot(planilha["T_SoluçãoIterativa"], planilha["QTD de Nº"], color = "blue")

    plt.title("Tempo de Solução - Iterativa x Recursiva")
    plt.xlabel("Tempo em Segundos")
    plt.ylabel("Quantidade Números da Lista/vetor (N)")

    plt.savefig("Grafico - Tempo das Soluções.png")
    plt.show()