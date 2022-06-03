medida1 = input("Insira o valor da medida A: ")
medida2 = input("Insira o valor da medida B: ")
medida3 = input("Insira o valor da medida C: ")

# Verificação dos dados Inseridos
if medida1 == "":
    print("Você não forneceu dados suficientes.")

elif medida2 == "":
    print("Você não forneceu dados suficientes.")

elif medida3 == "":
    print("Você não forneceu dados suficientes.")

try:
    medida1 = int(medida1)
    medida2 = int(medida2)
    medida3 = int(medida3)
except:
    raise Exception(
        "variável não é inteiro"
    )  # Exceção para quando usuário não insere um dado inteiro


# Verificação dos dados para saber se podem formar um triângulo ou não
if int(medida1) <= 0:
    print("As medidas não podem formar um triângulo.")

elif int(medida2) <= 0:
    print("As medidas não podem formar um triângulo.")

elif int(medida3) <= 0:
    print("As medidas não podem formar um triângulo.")

# Mostra qual tipo de triângulo é e quais foram as medidas inseridas.
elif medida1 == medida2 and medida2 == medida3:
    print("Seu triângulo é Equilátero e as medidas são: \n")
    print("medida A: " + str(medida1))
    print("medida B: " + str(medida2))
    print("medida C: " + str(medida3))

elif medida1 != medida2 and medida2 == medida3 or medida3 == medida1:
    print("Seu triângulo é isósceles e as medidas são: \n")
    print("medida A: " + str(medida1))
    print("medida B: " + str(medida2))
    print("medida C: " + str(medida3))

elif medida1 != medida2 and medida2 != medida3 and medida1 != medida3:
    print("Seu triângulo é Escaleno e as medidas são: \n")
    print("medida A: " + str(medida1))
    print("medida B: " + str(medida2))
    print("medida C: " + str(medida3))

elif medida1 == medida2 and medida2 != medida3:
    print("Seu triângulo é isósceles e as medidas são: \n")
    print("medida A: " + str(medida1))
    print("medida B: " + str(medida2))
    print("medida C: " + str(medida3))
