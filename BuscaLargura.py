#!/usr/bin/python3
##################################################################################
#
#                 NOME DO PROGRAMA: BuscaLargura.py                 
#  
#  DESCRIÇÃO: Algoritmo responsavel por realizar uma busca do tipo largura e
#             retornar o caminho encontrado, caso não ache retorna 0
#
#  AUTOR: Allainn Christiam Jacinto Tavares
#  
#  NOME DO PROJETO: Projeto estilos de busca em um mapa 
#
#  INSTITUIÇÃO: UTFPR
#
###################################################################################

import time
import Mapa as mp
import Redundancia as rd

# Função que realiza a busca
# Retorna caminho se encontrado
# Senão retorna 0
def largura():
    fila = []
    estado = rd.inicio
    mark = []
    mark.append(estado)
    caminho={}
    caminho[rd.inicio.i, rd.inicio.j] = [-1,-1]
    while(True):
        if rd.eh_objetivo(estado):
            print("Achou\nExpandidos:", end=" ")
            for i in mark:
                print("(",i.i, i.j,")", end=" ")
            print("\n\nTotal Expandidos = ",len(mark))
            k=[estado.i,estado.j]
            c=[]
            while(k != [-1,-1]):
                c.insert(0,k)
                k = caminho[k[0],k[1]]
            time.sleep(3)
            return c

        else:
            aux = (rd.sucessores(estado))
            flag = False
            for i in aux:
                for j in mark:
                    if i.i == j.i and i.j == j.j:
                        flag = True
                        break
                if not(flag):
                    caminho[i.i, i.j] = [estado.i,estado.j]
                    mark.append(i)
                    fila.append(i)
                flag = False

        if fila == []:
            print("Falhou")
            return 0
        estado = fila.pop(0)
