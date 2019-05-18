#!/usr/bin/python3
##################################################################################
#
#                 NOME DO PROGRAMA: Mapa.py                 
#  
#  DESCRIÇÃO: Algoritmo que contem as funções de controle sobre o mapa, como:
#             Retornar o Mapa e Imprimir o mapa. Neste algoritmo também contem
#             as variaveis de cores para cada tipo de terreno no mapa.
#
#  AUTOR: Allainn Christiam Jacinto Tavares
#  
#  NOME DO PROJETO: Projeto estilos de busca em um mapa 
#
#  INSTITUIÇÃO: UTFPR
#
###################################################################################

import random

VERDE = "\033[42m"
CINZA = "\033[100m"
AMARELO = "\033[43m"
MARROM = "\033[41m"
PRETO = "\033[40m"
RESET = "\033[0m"
NEGRITO = "\033[1m"
BRANCO = "\033[37m"

MURO = 0
SOLIDO = 1
ARENOSO = 4
ROCHOSO = 10
PANTANO = 20

TERRENOS = (MURO, SOLIDO, ARENOSO, ROCHOSO, PANTANO)

inicio = None
fim = None

def retornarMapaRandom():
    global inicio, fim
    MAPA = []

    inicio = [random.randrange(1,19), random.randrange(1,19)]
    fim = [random.randrange(1,19), random.randrange(1,19)]
    for i in range(20):
        MAPA.append([0]*20)

    for i in range(20):
        for j in range(20):
            if i == 0 or j == 0:
                MAPA[i][j] = MURO
            elif i == 19 or j == 19:
                MAPA[i][j] = MURO
            elif (inicio[0] == i and inicio[1] == j) or (fim[0] == i and fim[1] == j):
                MAPA[i][j] = TERRENOS[random.randrange(1,5)]
            else:
                MAPA[i][j] = TERRENOS[random.randrange(5)]
    return MAPA

def retornarMapa01():
    global inicio, fim
    inicio = [1,9]
    fim = [18,18]
    MAPA = [[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
            [0 ,10,10,10,10,10,20,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,10,10,1 ,0 ],
            [0 ,0 ,0 ,0 ,10,10,0 ,1 ,1 ,1 ,1 ,1 ,20,1 ,1 ,1 ,1 ,10,1 ,0 ],
            [0 ,4 ,4 ,0 ,10,10,10,1 ,1 ,1 ,1 ,1 ,0 ,10,4 ,0 ,20,20,0 ,0 ],
            [0 ,4 ,4 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,10,0 ,0 ,10,4 ,20,20,4 ,1 ,0 ],
            [0 ,4 ,4 ,4 ,4 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,10,1 ,0 ,1 ,0 ,1 ,0 ],
            [0 ,4 ,4 ,4 ,4 ,1 ,1 ,1 ,0 ,0 ,0 ,10,0 ,0 ,10,0 ,1 ,0 ,1 ,0 ],
            [0 ,20,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],
            [0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,4 ,0 ,10,10,0 ,4 ,0 ,0 ,0 ,1 ,0 ,0 ],
            [0 ,1 ,1 ,1 ,4 ,1 ,1 ,0 ,10,0 ,1 ,20,0 ,10,10,10,0 ,1 ,0 ,0 ],
            [0 ,4 ,4 ,0 ,0 ,1 ,1 ,0 ,10,0 ,4 ,4 ,0 ,0 ,0 ,0 ,0 ,1 ,4 ,0 ],
            [0 ,20,20,0 ,1 ,1 ,1 ,0 ,10,4 ,1 ,1 ,1 ,1 ,10,1 ,1 ,1 ,4 ,0 ],
            [0 ,20,20,0 ,4 ,0 ,0 ,0 ,20,0 ,1 ,1 ,10,10,10,0 ,0 ,0 ,1 ,0 ],
            [0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,20,0 ,0 ,20,0 ,0 ,0 ,0 ,20,0 ,1 ,0 ],
            [0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,10,10,1 ,1 ,1 ,20,20,20,0 ,1 ,0 ],
            [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,10,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],
            [0 ,0 ,1 ,1 ,1 ,1 ,4 ,4 ,4 ,0 ,10,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],
            [0 ,10,10,0 ,0 ,10,0 ,0 ,0 ,0 ,10,1 ,0 ,1 ,4 ,0 ,0 ,0 ,20,0 ],
            [0 ,10,10,1 ,1 ,10,4 ,1 ,4 ,1 ,10,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],
            [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]]

    return MAPA

def retornarMapa02():
    MAPA = [[0,0,0,0,0,0],
            [0,1,1,1,1,0],
            [0,0,4,0,5,0],
            [0,1,2,0,5,0],
            [0,1,3,1,1,0],
            [0,0,0,0,0,0]]

    return MAPA

def imprimirMatriz(MAPA):
    for i in range(len(MAPA)):
        for j in range(len(MAPA)):
            print(MAPA[i][j],end=" ")
        print()
    print()

def imprimirMapa(MAPA):
    aux=" "
    for i in range(len(MAPA)):
        for j in range(len(MAPA)):
            if inicio[0] == i and inicio[1] == j:
                aux = BRANCO+NEGRITO+"@"
            elif fim[0] == i and fim[1] == j:
                aux = BRANCO+NEGRITO+"F"
            else:
                aux = " "
            
            if MAPA[i][j] == 0:
                print(PRETO+" "+RESET,end="")
            elif MAPA[i][j] == 1:
                print(VERDE+aux+RESET,end="")
            elif MAPA[i][j] == 3:
                print(BRANCO+VERDE+NEGRITO+"@"+RESET,end="")
            elif MAPA[i][j] == 4:
                print(AMARELO+aux+RESET,end="")
            elif MAPA[i][j] == 6:
                print(BRANCO+AMARELO+NEGRITO+"@"+RESET,end="")
            elif MAPA[i][j] == 10:
                print(CINZA+aux+RESET,end="")
            elif MAPA[i][j] == 12:
                print(BRANCO+CINZA+NEGRITO+"@"+RESET,end="")
            elif MAPA[i][j] == 20:
                print(MARROM+aux+RESET,end="")
            elif MAPA[i][j] == 22:
                print(BRANCO+MARROM+NEGRITO+"@"+RESET,end="")
        print()