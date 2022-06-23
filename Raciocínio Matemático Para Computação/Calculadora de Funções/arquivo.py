"""
Desenvolvedor: Eric Henrique Banak e Jefferson III
Curso: Sistemas de Informação - Noturno
Objetivo: Desenvolver uma calculadora com menus aninhados, para realizar, com
persistência de dados, cálculos de funções Exponenciais, do segundo grau, e cálculos com matrizes.
Data: 23/06/2022 - Entrega do protótipo final da calculadora RMC.
"""

# imports
import sys
import numpy as np
import matplotlib.pyplot as plt
import cmath

# main
def main():

    input_menu = None

    while input_menu != "4":
        if input_menu not in (None, "1", "2", "3", "4"):
            print("\nOpcão Inválida, digite novamente.\n")

        print("\n---------------------------")
        print("MENU CALCULADORA RMC - ERIC HENRIQUE BANAK E JEFFERSON III")
        print("1 - Funções do Segundo Grau")
        print("2 - Exponenciais")
        print("3 - Matrizes")
        print("4 - Sair\n")
        input_menu = input("Opcão desejada: ")

        if input_menu == "1":
            calcular_funcao_segundo_grau()
        elif input_menu == "2":
            calcular_func_exponencial()
        elif input_menu == "3":
            calcular_matriz()
        elif input_menu == "4":
            sys.exit()


# Funções do segundo grau


def calcular_funcao_segundo_grau():
    input_sub_menu = None

    while input_sub_menu != "7":
        if input_sub_menu not in (None, "1", "2", "3", "4", "5", "6", "7"):
            print("\nOpcão Inválida, digite novamente.\n")

        print("\n---------------------------")
        print("\nMENU de Funções do 2o Grau")
        print("1 - Calcular raízes")
        print("2 - Verificação Crescente ou Decrescente")
        print("3 - Calcular f(x) ou função de X")
        print("4 - Cálculo do Vértice")
        print("5 - Gerar gráfico")
        print("6 - Voltar")
        print("7 - Sair\n")
        input_sub_menu = input("Opção desejada: ")

        if input_sub_menu == "1":
            calcular_raizes()
        elif input_sub_menu == "2":
            verificacao_crescente_decrescente_func_segundo_grau()
        elif input_sub_menu == "3":
            calcular_funcao_x()
        elif input_sub_menu == "4":
            calcular_vertice()
        elif input_sub_menu == "5":
            gerar_grafico_func_segundo_grau()
        elif input_sub_menu == "6":
            break  # voltar
        elif input_sub_menu == "7":
            sys.exit()


def raizes(a, b, c):
    D = b**2 - 4 * a * c  # cálculo do delta
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    x2 = (-b - D ** (1 / 2)) / (2 * a)

    print("\nValor de x1: {0}".format(x1))
    print("Valor de x2: {0}".format(x2))


def calcular_raizes():
    print("Calculando as raízes de uma equação de 2º grau\n")
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))
    raizes(a, b, c)


def verificacao_crescente_decrescente_func_segundo_grau():
    valor_de_a = None
    while not valor_de_a:
        try:
            valor_de_a = int(
                input("Insira o valor de a para confirmar a verificação: ")
            )
            if valor_de_a < 1:
                raise Exception("aaa")
        except:
            print("\nValor inválido, digite novamente.")
            valor_de_a = None

    if valor_de_a > 1:
        print("\nA função de segundo grau é crescente, pois a > 1.\n")
    elif 0 < valor_de_a < 1:
        print("\nA função é descrescente pois 0 < a < 1.\n")
    else:
        print("\nO valor inserido não é válido.\n")


def calcular_funcao_x():
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))

    # calcular delta
    d = (b**2) - (4 * a * c)

    # achar duas soluções
    solucao1 = (-b - cmath.sqrt(d)) / (2 * a)
    solucao2 = (-b + cmath.sqrt(d)) / (2 * a)
    print("As soluções são {0} e {1}".format(solucao1, solucao2))


def calcular_vertice():
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))
    y_vertice = ((b * b) - (4 * a * c)) / (-4 * a)
    x_vertice = -b / (2 * a)
    print(f"O cálculo do vértice da função resultou em: {x_vertice}, {y_vertice}")


def gerar_grafico_func_segundo_grau():
    a = int(input("Entre com o valor de a (ex: -10): "))
    b = int(input("Entre com o valor de b (ex: 10): "))

    x = np.linspace(a, b, 100)  # 100 numeros espaçados igualmente
    y = x**2  # função

    # setando eixos
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    # plotar a função
    plt.plot(x, y, "r")

    # mostra o gráfico
    plt.show()


# Funções Exponenciais


def calcular_func_exponencial():
    input_sub_menu = None

    while input_sub_menu != "6":

        if input_sub_menu not in (None, "1", "2", "3", "4", "5", "6"):
            print("\nOpcão Inválida, digite novamente.\n")

        print("\n---------------------------")
        print("\nMENU de Funções Exponenciais")
        print("1 - Verificação de Existência")
        print("2 - Verificação Crescente ou Decrescente")
        print("3 - Calcular f(x) ou função de X")
        print("4 - Gerar gráfico")
        print("5 - Voltar")
        print("6 - Sair\n")

        input_sub_menu = input("Opcão desejada: ")  # ! Tá saindo quando nao digita nada

        if input_sub_menu == "1":
            verificar_existencia()
        elif input_sub_menu == "2":
            verificar_crescente_decrescente_func_exponencial()
        elif input_sub_menu == "3":
            print("Função: x**2")
            x = int(input("Insira o valor de x: "))
            calcular_funcao_x_func_exponencial(x)
        elif input_sub_menu == "4":
            grafico_func_exponencial()

        # voltar
        elif input_sub_menu == "5":
            break
        elif input_sub_menu != "6":
            sys.exit()


def verificar_existencia():
    valor_da_base = int(input("Insira o valor de a para verificar existência: "))

    if valor_da_base <= 0:
        print("Não é função exponencial.")
    elif valor_da_base == 1:
        print("Não é função exponencial.")
    elif valor_da_base > 1:
        print("É função exponencial.")


def verificar_crescente_decrescente_func_exponencial():
    valor_de_a = None
    while not valor_de_a:
        try:
            valor_de_a = int(
                input("Insira o valor de a para confirmar a verificação: ")
            )
            if valor_de_a < 1:
                raise Exception("aaa")
        except:
            print("\nValor inválido, digite novamente.")
            valor_de_a = None

    if valor_de_a > 1:
        print("\nA função exponencial é crescente, pois a > 1.\n")
    elif 0 < valor_de_a < 1:
        print("\nA função é descrescente pois 0 < a < 1.\n")
    else:
        print("\nO valor inserido não é válido.\n")


def calcular_funcao_x_func_exponencial(x):
    valor_de_a = int(input("Insira o valor de a: "))

    resultado = x**2
    print(f"O valor encontrado para f({x}) foi: ", {resultado})

    return valor_de_a * (x**2)


def funcaoExponencial(a, x):
    return a**x


def grafico_func_exponencial():
    vetorX = np.arange(-7, 7, 0.1)
    print(vetorX)

    a = 2
    vetorY = []
    for x in vetorX:
        vetorY.append(funcaoExponencial(a, x))
    print(vetorY)

    fig = plt.figure(figsize=(5, 5))

    plt.plot(vetorX, vetorY, label="Funcao Exponencial", color="g")

    plt.title("f(x) = a^x")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.show()
    fig.savefig("FExp.png")


# Funções de Matriz


def calcular_matriz():

    print("\n---------------------------")
    print("MENU de Matrizes")
    print("Criando uma matriz...\n")

    matriz, nr_linhas, nr_colunas = get_input_matriz()

    input_sub_menu = None

    while input_sub_menu != "5":

        if input_sub_menu not in (None, "1", "2", "3", "4", "5"):
            print("\nOpcão Inválida, digite novamente.\n")

        print("\n---------------------------")
        print("MENU de Matrizes")
        print("1. Verificar determinante")
        print("2. Multiplicação")
        print("3. Matriz Transposta")
        print("4. Voltar")
        print("5. Sair")
        input_sub_menu = input("Opcão desejada: ")

        if input_sub_menu == "1":
            matriz_determinante(nr_linhas, nr_colunas)
        elif input_sub_menu == "2":
            print("\nCriando uma segunda matriz...\n")
            matriz2, nr_linhas2, nr_colunas2 = get_input_matriz_secundaria()
            multiplicacao_matriz(
                nr_linhas, nr_linhas2, nr_colunas, nr_colunas2, matriz, matriz2
            )

        elif input_sub_menu == "3":
            matriz_transposta(matriz)

        # voltar
        elif input_sub_menu == "4":
            break
        elif input_sub_menu == "5":
            sys.exit()


def matriz_determinante(nr_linhas, nr_colunas):
    if nr_linhas == nr_colunas:
        print(
            f"\nSua matriz é quadrada. Representada pelo determinante {nr_linhas} x {nr_colunas}"
        )
    else:
        print("\nSua matriz não é quadrada.")


def multiplicacao_matriz(
    nr_linhas, nr_linhas2, nr_colunas, nr_colunas2, matriz, matriz2
):
    if nr_linhas == nr_linhas2:
        if nr_colunas == nr_colunas2:
            print("\nA multiplicação é possível!")
            np.squeeze(np.asarray(matriz))
            np.squeeze(np.asarray(matriz2))
            print(np.dot(matriz, matriz))

    elif nr_colunas == nr_colunas2:
        if nr_linhas == nr_linhas2:
            print("\nA multiplicação é possível!")
            np.squeeze(np.asarray(matriz))
            np.squeeze(np.asarray(matriz2))
            print(np.dot(matriz, matriz))

    else:
        print("A multiplicação não é possível.")


def matriz_transposta(matriz):
    np.squeeze(np.asarray(matriz))
    transposta = np.transpose(matriz)
    print(transposta)


def get_input_matriz():
    matriz = []
    # input matriz
    nr_linhas = None
    nr_colunas = None

    # input + validação numero de linhas
    while not nr_linhas:
        try:
            nr_linhas = int(input("Insira o número de linhas da matriz: "))
            if nr_linhas < 1:
                raise Exception("aaa")
        except:
            print("\nValor inválido, digite novamente.")
            nr_linhas = None

    # input + validação numero de colunas
    while not nr_colunas:
        try:
            nr_colunas = int(input("Insira o número de colunas da matriz: "))
            if nr_colunas < 1:
                raise Exception()
        except:
            print("\nValor inválido, digite novamente.")
            nr_colunas = None

    # input valores da matriz
    for count_linha in range(0, int(nr_linhas)):
        print("\nLinha: ", count_linha)
        linha = []  # Cria lista vazia para adicionar elementos

        for count_coluna in range(0, int(nr_colunas)):
            elemento = int(input("Digite o próximo elemento: "))
            while elemento == "":
                try:
                    elemento = input("Por favor, insira um número válido: \n")
                    break
                except ValueError:
                    print("\nOops! Isso não é um número válido, tente novamente.")

            linha.append(elemento)  # Adiciona elemento à linha
        matriz.append(linha)  # Adiciona linha à matriz

    print("\nSua matriz é: ")
    for linha in matriz:
        print(linha)

    return matriz, nr_linhas, nr_colunas


def get_input_matriz_secundaria():
    matriz2 = []
    # input matriz
    nr_linhas2 = None
    nr_colunas2 = None

    # input + validação numero de linhas
    while not nr_linhas2:
        try:
            nr_linhas2 = int(input("Insira o número de linhas da segunda matriz: "))
            if nr_linhas2 < 1:
                raise Exception("aaa")
        except:
            print("\nValor inválido, digite novamente.")
            nr_linhas2 = None

    # input + validação numero de colunas
    while not nr_colunas2:
        try:
            nr_colunas2 = int(input("Insira o número de colunas da segunda matriz: "))
            if nr_colunas2 < 1:
                raise Exception()
        except:
            print("\nValor inválido, digite novamente.")
            nr_colunas2 = None

    # input valores da matriz
    for count_linha in range(0, int(nr_linhas2)):
        print("\nLinha: ", count_linha)
        linha_secundaria = []  # Cria lista vazia para adicionar elementos

        for count_coluna in range(0, int(nr_colunas2)):
            elemento = int(input("Digite o próximo elemento: "))
            while elemento == "":
                try:
                    elemento = input("Por favor, insira um número válido: \n")
                    break
                except ValueError:
                    print("\nOops! Isso não é um número válido, tente novamente.")

            linha_secundaria.append(elemento)  # Adiciona elemento à linha
        matriz2.append(linha_secundaria)  # Adiciona linha à matriz

    print("\nSua segunda matriz é (USADA APENAS PARA MULTIPLICAÇÃO): ")
    for linha_secundaria in matriz2:
        print(linha_secundaria)

    return matriz2, nr_linhas2, nr_colunas2


# chamada do main
if __name__ == "__main__":
    main()
