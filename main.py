from cadastro_cartas import(cadastro_jogador, cadastro_cartas, exibir_carta)
from time import sleep


print("=-="*20)
print("##  Bem Vindo ao Jogo: Super-Trunfo  ##")
print("=-="*20)
jogador1 = cadastro_jogador()
sleep(0.5)
carta1 = cadastro_cartas()
exibir_carta(jogador1, *carta1)
