#!/usr/bin/python3
##################################################################################
#
#                 NOME DO PROGRAMA: Redundancia.py                 
#  
#  DESCRIÇÃO: Algoritmo que contem as função que são redundantes entre os
#             estilos de busca, como: Manter o MAPA, a classe No, o ponto
#             inicial e final da busca, verificar se o no é o objetivo e
#             expandir os filhos de um determinado no.
#
#  AUTOR: Allainn Christiam Jacinto Tavares
#  
#  NOME DO PROJETO: Projeto estilos de busca em um mapa 
#
#  INSTITUIÇÃO: UTFPR
#
###################################################################################

import Mapa as mp

inicio = None
fim = None

MAPA = mp.retornarMapa01() 
def resetMapa():
    global MAPA, inicio, fim
    MAPA = mp.retornarMapa01()
    inicio = No(mp.inicio[0],mp.inicio[1])
    fim = No(mp.fim[0],mp.fim[1])

def randMapa():
    global MAPA, inicio, fim
    MAPA = mp.retornarMapaRandom()
    inicio = No(mp.inicio[0],mp.inicio[1])
    fim = No(mp.fim[0],mp.fim[1])

class No(object):
    def __init__(self, i, j, custo=0):
        self.i = i
        self.j = j
        self.custo = custo
        self.heuristica = 0
        self.fn = 0

    def __eq__(self, value):
        return (self.i == value.i and self.j == value.j and self.fn == value.fn)
    
    def calcularFn(self):
        self.fn = self.heuristica + self.custo


def eh_objetivo(estado):
    if estado.i == fim.i and estado.j == fim.j:
        return True
    else:
        return False

def sucessores(estado, informada=False):
    filho = []

    if MAPA[estado.i+1][estado.j] != 0:
        no = No(estado.i+1,estado.j)
        if informada:
            no.custo = estado.custo
            h=(abs(no.i-fim.i)+abs(no.j-fim.j))
            no.heuristica = h
            no.custo+=MAPA[no.i][no.j]
            no.calcularFn()
        filho.append(no)
    
    if MAPA[estado.i][estado.j+1] != 0:
        no=No(estado.i,estado.j+1)
        if informada:
            no.custo = estado.custo
            no.custo+=MAPA[no.i][no.j]
            h=(abs(no.i-fim.i)+abs(no.j-fim.j))
            no.heuristica = h
            no.calcularFn()
        filho.append(no)
    
    if MAPA[estado.i-1][estado.j] != 0:
        no=No(estado.i-1,estado.j)
        if informada:
            no.custo = estado.custo
            no.custo+=MAPA[no.i][no.j]
            h=(abs(no.i-fim.i)+abs(no.j-fim.j))
            no.heuristica = h
            no.calcularFn()
        filho.append(no)
    
    if MAPA[estado.i][estado.j-1] != 0:
        no=No(estado.i,estado.j-1)
        if informada:
            no.custo = estado.custo
            no.custo+=MAPA[no.i][no.j]
            h=(abs(no.i-fim.i)+abs(no.j-fim.j))
            no.heuristica = h
            no.calcularFn()
        filho.append(no)
    return filho