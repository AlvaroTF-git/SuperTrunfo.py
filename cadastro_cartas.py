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



    
