#!/bin/us/python3
##################################################################################
#
#                 NOME DO PROGRAMA: Principal.py                 
#  
#  DESCRIÇÃO: Algoritmo responsavel por solicitar ao usuario qual estilo de 
#             busca ele deseja utilizar e também mostrar qual caminho do 
#             ponto inicial até o objetivo
#
#  AUTOR: Allainn Christiam Jacinto Tavares
#  
#  NOME DO PROJETO: Projeto estilos de busca em um mapa 
#
#  INSTITUIÇÃO: UTFPR
#
###################################################################################

import BuscaLargura as bl
import BuscaAEstrela as ba
import BuscaProfundidade as bp
import Mapa as mp
import Redundancia as rd
import time

# Função que mostra o caminho percorrido no mapa
def mostrarCaminho(caminho):
    # print("\nCAMINHO:",caminho)
    contRecompensas = 0
    custo = -(rd.MAPA[rd.inicio.i][rd.inicio.j])
    for i in caminho:
        time.sleep(0.5)
        custo += rd.MAPA[i[0]][i[1]]
        if i in mp.recompensas:
            contRecompensas += 1
        rd.MAPA[i[0]][i[1]]+=2
        mp.imprimirMapa(rd.MAPA)
    print("Custo Total = "+str(custo))
    print("Recompensas = "+str(contRecompensas))

# Função princial que solicita ao usuario realizar uma escolha de um estilo de busca
if __name__ == "__main__":
    while(True):
        rd.resetMapa()
        print("Mapa Padrão")
        mp.imprimirMapa(rd.MAPA)
        print("Deseja gerar mapa aleatorio? (s) ")
        res = input()
        if res == 's':
            rd.randMapa()
            mp.imprimirMapa(rd.MAPA)

        print('''Digite:
        1 - BUSCA EM LARGURA
        2 - BUSCA EM PROFUNDIDADE
        3 - BUSCA A ESTRELA
        4 - SAIR''')
        op = input()

        if op == '1':
            print("--- BUSCA EM LARGURA ---")
            print("BUSCANDO....")
            caminho=bl.largura()
            if caminho:
                mostrarCaminho(caminho)
            print("--- BUSCA EM LARGURA ---\n\n")
            time.sleep(5)
        elif op == '2':
            print("--- BUSCA EM PROFUNDIDADE ---")
            print("BUSCANDO....")
            caminho=bp.profundidade()
            if caminho:
                mostrarCaminho(caminho)
            print("--- BUSCA EM PROFUNDIDADE ---\n\n")
            time.sleep(5)    
        elif op == '3':
            print("--- BUSCA A ESTRELA ---")
            print("BUSCANDO....")
            caminho=ba.aEstrela()
            if caminho:
                mostrarCaminho(caminho)
            print("--- BUSCA A ESTRELA ---\n\n")
            time.sleep(5)
        elif op == '4':
            exit(1)
        else:
            print("Operação Invalida\n")
