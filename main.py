from cadastro_cartas import(cadastro_jogador, cadastro_cartas, exibir_carta, interface_main, interface_comparacao, comparacao,interface_game)
from time import sleep

game = 1
print("=-="*20)
print("##  Bem Vindo ao Jogo: Super-Trunfo  ##")
print("=-="*20)
opcao = interface_main()
if opcao == 1:
        ##cadastro do primeiro jogador
        print("--- Cadastrando o primeiro jogador ---")
        jogador1 = cadastro_jogador()
        sleep(0.5)
        carta1 = cadastro_cartas()
        exibir_carta(jogador1, *carta1)
        sleep(0.5)
        ##cadastro do segundo jogador jogador
        print("--- Cadastrando o Segundo jogador ---")
        jogador2 = cadastro_jogador()
        sleep(0.5)
        carta2 = cadastro_cartas()
        exibir_carta(jogador2, *carta2)
elif opcao == 2:
        print("Encerrando o programa...")

while True:
    escolha = interface_game()
    if escolha == 1:
        escolha_atributo = interface_comparacao()
        if escolha_atributo == 1:
              comparacao(escolha_atributo, carta1, carta2)
              break
        if escolha_atributo == 2:
              comparacao(escolha_atributo, carta1, carta2)
              break
    elif escolha == 2:
        exibir_carta(jogador1, carta1[0], carta1[1],carta1[2],carta1[3])
        exibir_carta(jogador2, carta2[0], carta2[1],carta2[2],carta2[3])
        sleep(10)
     
print("Encerrando o programa...")
              