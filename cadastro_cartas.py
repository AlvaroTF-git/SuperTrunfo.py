from time import sleep

def cadastro_cartas():
    codigo = str(input('Digite o código da sua carta, EX -> A99\nCÓDIGO: ')).strip()
    estado = str(input('Digite a sigla do Estado, EX -> PE\nESTADO: ')).strip()
    populacao = int(input('Digite a população do Estado, EX -> 1000\nPOPULAÇÃO: '))
    pontos_turisticos = int(input('Digite a quantidade de pontos Turísticos. EX -> 50\nPONTOS TURÍSTICOS: '))
    print("=-"*20)
    return codigo,estado,populacao,pontos_turisticos

def cadastro_jogador():
    print("=-"*20)
    print("### Cadastro de jogadores ###")
    nickname = str(input("Digite seu nome: ")).strip()
    print(f"Jogador registrado: {nickname}")
    print("=-="*20)
    return nickname

def exibir_carta(nickname, codigo, estado, populacao, pontos_turisticos):
    print(f'Carta do Jogador: {nickname}')
    print(f'CÓDIGO: {codigo}')
    print(f'ESTADO: {estado}')
    print(f'POPULAÇÃO: {populacao}\nPontos TURÍSTICOS: {pontos_turisticos}')
    print("=-="*20)

def interface_main():
    print("Opções do Programa: ")
    print("1. começar o jogo")
    print("2. encerrar o programa")
    opcao = int(input("Digite uma opção: "))
    return opcao


def interface_comparacao():
    print("Escolha um atributo para comparar: ")
    print(f"1. População")
    print(f"2. Pontos Turísticos")
    inter_comparacao = int(input("Digite um número: "))
    return inter_comparacao

def comparacao(escolha_atributo, carta1, carta2):
    if escolha_atributo == 1:
        crit = 2
        sleep(0.5)
        print("==="*13)
        print("A comparação escolhida é: população!!")
        print(f"População da primeira carta --> {carta1[crit]}\nPopulação da segunda carta --> {carta2[crit]} ")
        print("==="*13)
        sleep(0.5)
        if carta1[crit] > carta2[crit]:
            print("### Jogador 1 venceu ###")
        elif carta1[crit] < carta2[crit]:
            print("### Jogador 2 venceu! ###")
        else:
            print("### Os jogadores empataram!! ###")
    if escolha_atributo == 2:
        crit = 3
        sleep(0.5)
        print("==="*13)
        print("A comparação escolhida é: Pontos Turísticos!!")
        print(f"População da primeira carta --> {carta1[crit]}\nPopulação da segunda carta --> {carta2[crit]} ")
        print("==="*13)
        sleep(0.5)
        if carta1[crit] > carta2[crit]:
            print("### Jogador 1 venceu ###")
        elif carta1[crit] < carta2[crit]:
            print("### Jogador 2 venceu! ###")
        else:
            print("### Os jogadores empataram!! ###")


def interface_game():
    print("1. Comparar atributo das cartas")
    print("2. Mostrar as cartas")
    print("3. Encerrar o programa")
    option = int(input("Digite a opção escolhida: "))
    return option