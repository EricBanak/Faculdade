"""
Desenvolvedor: Eric Henrique Banak
Curso: Análise e Desenvolvimento de Sistemas (EAD)
Objetivo: Criar o jogo Zombie Dice para projeto da matéria.
Data: 20/09/2021 - Entrega do protótipo final do jogo Zombie Dice.
"""

import random
import sys


class Jogador:
    def __init__(self, nome, nr_cerebros=0, nr_tiros=0, jogador_vivo=True):
        self.nome = nome
        self.nr_cerebros = nr_cerebros
        self.nr_tiros = nr_tiros
        self.jogador_vivo = jogador_vivo

    def morrer(self):
        self.jogador_vivo = False


def pegar_dado_do_copo():

    global mao_jogador
    global copo

    # Sorteia os 3 dados do copo
    while len(mao_jogador) < 3:
        dado = random.choice(copo)  # Selecionando de forma randômica dado do copo

        # Incluindo dado selecionado na mão do jogador
        mao_jogador.append(dado)
        copo.remove(dado)


def inicializa_dados_copo():
    # Criar uma estrutura de dados utilizando uma string (6 verdes, 4 amarelos e 3 vermelhos)
    copo_default = [
        ("Verde", ("C", "P", "C", "T", "P", "C")),
        ("Verde", ("C", "P", "C", "T", "P", "C")),
        ("Verde", ("C", "P", "C", "T", "P", "C")),
        ("Verde", ("C", "P", "C", "T", "P", "C")),
        ("Verde", ("C", "P", "C", "T", "P", "C")),
        ("Verde", ("C", "P", "C", "T", "P", "C")),
        ("Amarelo", ("T", "P", "C", "T", "P", "C")),
        ("Amarelo", ("T", "P", "C", "T", "P", "C")),
        ("Amarelo", ("T", "P", "C", "T", "P", "C")),
        ("Amarelo", ("T", "P", "C", "T", "P", "C")),
        ("Vermelho", ("T", "P", "T", "C", "P", "T")),
        ("Vermelho", ("T", "P", "T", "C", "P", "T")),
        ("Vermelho", ("T", "P", "T", "C", "P", "T")),
    ]
    return copo_default


def lancar_dados():

    global passos
    global jogador
    global mao_jogador
    global lista_mesa

    lista_mesa = []

    # Rotina para jogar e sortear a face dos dados
    for dado in mao_jogador:
        face = random.choice(dado[1])
        # Incrementa as variáveis quando um dos dados é lançado
        if face == "P":
            passos = passos + 1
        elif face == "C":
            # cerebros = cerebros + 1
            jogador.nr_cerebros += 1
        elif face == "T":
            jogador.nr_tiros += 1

        # Verificar o resultado dos tres dados lancados
        print(f"Dado { dado[0] }, com a face: { face }, virada para cima.")
        lista_mesa.append((dado, face))  # Appenda dado e face virada na lista_mesa

    mao_jogador = []


def apresentar_pontuacao_turno():

    global passos
    global jogador

    print("\nNúmero de cérebros: ", jogador.nr_cerebros)
    print("Número de passos: ", passos)
    print("Número de tiros: ", jogador.nr_tiros)


def printar_os_dados_do_copo():

    global copo

    print(f"\nDados do copo: ({len(copo)})")
    for dado in copo:
        print(dado[0])


def verifica_jogador_ganhou_ou_perdeu():
    """
    Se jogador morreu, retorna False.
    Se ganhou, printa na tela e finaliza jogo.
    Se jogador está vivo, retorna True.
    """

    global jogador
    global turno_ativo
    global lista_jogadores

    # Se o jogador tomar 3 tiros ou mais, ele morre
    if jogador.nr_tiros >= 3:
        print(f"\nGAME OVER - Jogador {jogador.nome} morto.")
        jogador.morrer()
        turno_ativo = False

    elif jogador.nr_cerebros >= 13:
        print(
            f"\nParabéns {jogador.nome}, você atingiu {jogador.nr_cerebros} cérebros, você ganhou o jogo!"
        )
        sys.exit()

    # Contar numero de jogadores vivos
    count_jogadores_vivos = 0
    for row in lista_jogadores:
        if row.jogador_vivo == True:
            count_jogadores_vivos += 1

            nome_ultimo_jogador = row.nome

    if count_jogadores_vivos <= 1:
        print(
            f"\nParabéns {nome_ultimo_jogador}, como você é o último jogador vivo, você ganhou o jogo.\n"
        )
        sys.exit()

    elif jogador.nr_tiros >= 3:
        # Jogador atual morto
        return False

    else:
        # Jogador atual vivo
        return True


def verifica_se_jogador_quer_continuar_turno():

    global jogador
    global turno_ativo

    # Verificar se o jogador quer continuar o turno
    opcao = input(f"\nJogador {jogador.nome}, você vai querer continuar? (s/n): \n")
    while opcao not in ("s", "n"):  # Validacao do input do usuario (s/n)
        opcao = input(
            f"\nOpção Inválida. Jogador {jogador.nome}, você vai querer continuar? (s/n): \n"
        )

    if opcao == "n":
        turno_ativo = False
        jogador.nr_tiros = 0  # Reinicia pontuacao de tiros no final do turno
        print("\nTurno finalizado.")


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

# Estrutura para armazenar jogadores
lista_jogadores = []

while len(lista_jogadores) < num_jogadores:
    nome_jogador = input("Insira o nome do jogador: ")
    jogador = Jogador(nome=nome_jogador)
    lista_jogadores.append(jogador)

# Inicializar dados do copo
copo_default = inicializa_dados_copo()

# Loop para validar se o jogo ainda nao foi encerrado
jogo_ativo = True
while jogo_ativo:

    # Loop de jogadores
    for jogador in lista_jogadores:

        passos = 0  # Zerar numero de passos no inicio de cada turno

        # Iniciar turno
        copo = copo_default.copy()  # Inicializa copo com todos os dados
        mao_jogador = []  # Inicializa mao do jogador vazia

        turno_ativo = True

        while turno_ativo and jogador.jogador_vivo:
            print("\n\n-----------------------------------------")
            print("\nInício do turno do jogador: ", jogador.nome)
            print("\nOs dados jogados apresentaram os seguintes resultados:")

            # Funcao pegar dados e funcao remover dados do copo
            pegar_dado_do_copo()

            # Lancar dados e printar cor do dado e face sorteada
            lancar_dados()

            # Apresentar pontuacao do jogo
            apresentar_pontuacao_turno()

            # Printar dados do copo
            printar_os_dados_do_copo()

            # Verifica se o jogador ganhou ou perdeu (retorno de valores conforme docstring foi descontinuado, devido a logica de classe de jogador)
            verifica_jogador_ganhou_ou_perdeu()

            # Se o jogador esta vivo, possibilita continuar o jogo, se nao,
            # vai para o proximo turno do proximo jogador.
            if jogador.jogador_vivo == False:
                continue

            # Apos jogar, os dados de face "Cerebro" e "Tiros" sao devolvidos
            # ao copo, e os dados da face "Passos" voltam para a mao do jogador
            for item in lista_mesa:
                dado = item[0]  # Extrai informacao do dado da lista_mesa
                face = item[1]  # Extrai face virada do dado da lista_mesa

                if face in ("C", "T"):
                    copo.append(dado)

                elif face == "P":
                    mao_jogador.append(dado)
            lista_mesa = []

            verifica_se_jogador_quer_continuar_turno()
