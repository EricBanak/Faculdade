"""
Desenvolvedor: Eric Henrique Banak
Curso: Análise e Desenvolvimento de Sistemas (EAD)
Objetivo: Criar o jogo Zombie Dice para projeto da matéria.
Data: 30/08/2021 - Checkpoint do projeto semana 4
"""

import random

# Criar os dados utilizando uma string (6 verdes, 4 amarelos e 3 vermelhos)
tubo_default = (
    "CPCTPC",
    "CPCTPC",
    "CPCTPC",
    "CPCTPC",
    "CPCTPC",
    "CPCTPC",
    "TPCTPC",
    "TPCTPC",
    "TPCTPC",
    "TPCTPC",
    "TPTCPT",
    "TPTCPT",
    "TPTCPT",
)

# Entrada para receber a quantidade de jogadores
print("Seja bem vindo ao Zombie Dice.")
print("Vamos começar...")

# Receber número de jogadores do input pelo teclado do usuario
num_jogadores = int(input("\nInforme o numero de jogadores: \n"))

# Efetua checagem se foi adicionado pelo menos dois jogadores
while num_jogadores < 2:
    num_jogadores = int(
        input("\nNumero de jogadores incorreto, informe o numero de jogadores: \n")
    )

#lista_jogadores = []
#nr_jogador = 1
#while nr_jogador <= num_jogadores:
#    jogador = {'nome':f'Jogador {nr_jogador}',
#               'nr_cerebros':0,
#               'jogador_vivo':True}
#    lista_jogadores.append(jogador)           
#    nr_jogador += 1
#
#
#jogo_ativo = True
#while jogo_ativo:
#
#    for jogador


# Inicializar variáveis para contabilizar tiros, cerebros e passos antes do inicio do turno
cerebros = 0
passos = 0
tiros = 0

# Iniciar turno
tubo = tubo_default  # Inicializa tubo com todos os dados
mao_jogador = []  # Inicializa mao do jogador vazia

turno_ativo = True
jogador_vivo = True

while turno_ativo and jogador_vivo:
    print("\nOs dados jogados apresentaram os seguintes resultados:")

    # Sorteia os 3 dados do tubo
    while len(mao_jogador) < 3:
        dado = random.choice(tubo)  # Selecionando de forma randômica dado do tubo

        # Incluindo dado selecionado na mão do jogador
        mao_jogador.append(dado)
        tubo.remove(dado)

    lista_mesa = []

    # Rotina para jogar e sortear a face dos dados
    for dado in mao_jogador:
        face = random.choice(dado)

        # Incrementa as variáveis quando um dos dados é lançado
        if face == "P":
            passos = passos + 1

        elif face == "C":
            cerebros = cerebros + 1

        elif face == "T":
            tiros = tiros + 1

        # Verificar o resultado dos tres dados lancados
        print(f"{ dado }, com a face: { face }, virada para cima.")
        lista_mesa.append((dado, face))  # Appenda dado e face virada na lista_mesa
    mao_jogador = []

    # Se o jogador tomar 3 tiros ou mais, ele perde o jogo
    if tiros >= 3:
        print("\nGAME OVER - Jogador morto.")
        jogador_vivo = False
        continue

    if cerebros >= 13:
        print("Parabens, voce ganhou o jogo!")
        continue
    
    # Apos jogar, os dados de face "Cerebro" e "Tiros" sao devolvidos 
    # ao tubo, e os dados da face "Passos" voltam para a mao do jogador.
    for item in lista_mesa:
        dado = item[0]  # Extrai informacao do dado da lista_mesa
        face = item[1]  # Extrai face virada do dado da lista_mesa

        if face in ('C', 'T'):
            tubo.append(dado)
        
        elif face == 'P':
            mao_jogador.append(dado)
    lista_mesa = []

    # Verificar se o jogador quer continuar o turno
    opcao = input("\nJogador, você vai querer continuar? (s/n): \n")
    while opcao not in ("s", "n"):  # Validacao do input do usuario (s/n)
        opcao = input("\nOpção Inválida, você vai querer continuar? (s/n): \n")

    if opcao == "n":
        turno_ativo = False
        tiros = 0  # Zera número de tiros por conta do final do turno
        print("\nTurno finalizado.")
