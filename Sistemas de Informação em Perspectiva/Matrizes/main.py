# A matriz é montada a partir de três listas, matriz comentada como exemplo:

"""
Row1 = [1, 2, 3] 
Row2 = [4, 5, 6] 
Row3 = [7, 8, 9]
"""

# Criando as linhas da matriz supondo que seja uma lista 3x3
linha1 = []
linha2 = []
linha3 = []

# ---- LINHA 1: ----
# Usando range para inserir linhas na matriz
for i in range(0, 3):
    valor = int(input("Insira o próximo valor da linha 1: "))

    linha1.append(valor)  # adicionando o elemento

print("Ok, você preencheu a primeira linha da matriz.\n")

# ---- LINHA 2: ----
for i in range(0, 3):
    valor2 = int(input("Insira o próximo valor da linha 2: "))

    linha2.append(valor2)

print("Beleza, você preencheu a segunda linha da matriz.\n")

# ---- LINHA 3: ----
for i in range(0, 3):
    valor3 = int(input("Insira o próximo valor da linha 3: "))

    linha3.append(valor3)

print("\n\n-----------------------------")
print("\nSua matriz resultou em:\n")
print(linha1)
print(linha2)
print(linha3)


# Em seguida, é realizado o cálculo da soma da diagonal 1, left to right (esquerda para a direita)
d1 = linha1[0] + linha2[1] + linha3[2]

# Então o cálculoo da diagonal 2, right to left (direita para a esquerda)
d2 = linha1[2] + linha2[1] + linha3[0]


# Cálculo do resultado da soma da diagonal 1, menos a soma da diagonal 2
d1_menos_d2 = d1 - d2

print("\nO resultado do cálculo da soma da diagonal 1, menos a diagonal 2 é: \n")

print(d1_menos_d2)
