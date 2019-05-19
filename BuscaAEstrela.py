#!/usr/bin/python3
##################################################################################
#
#                 NOME DO PROGRAMA: BuscaAEstrela.py                 
#  
#  DESCRIÇÃO: Algoritmo responsavel por realizar uma busca do tipo A* e
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
import operator
import Mapa as mp
import Redundancia as rd

# Função que realiza a busca
# Retorna caminho se encontrado
# Senão retorna 0
def aEstrela():
    fila = []
    estado = rd.inicio
    h=estado.custo*(abs(estado.i-rd.fim.i)+abs(estado.j-rd.fim.j))
    estado.heuristica = h
    mark = []
    mark.append(estado)
    caminho={}
    caminho[rd.inicio.i, rd.inicio.j] = [-1,-1,-1]
    while(True):
        if(rd.eh_objetivo(estado)):
            print("Achou\nExpandidos:", end=" ")
            for i in mark:
                print("(",i.i, i.j,")", end=" ")
            print("\n\nTotal Expandidos = ",len(mark))
            k=[estado.i,estado.j,estado.fn]
            c=[]
            while(k != [-1,-1]):
                c.insert(0,k)
                k = caminho[k[0],k[1]][:-1]
            time.sleep(3)
            return c

        else:
            aux = rd.sucessores(estado, True)
            flag = False
            for i in aux:
                for j in mark:
                    if i.__eq__(j):
                        flag = True
                        break
                if not(flag):
                    mark.append(i)
                    try:
                        if i.fn < caminho[i.i, i.j][2]:
                            caminho[i.i, i.j] = [estado.i,estado.j, i.fn]
                    except KeyError:
                        caminho[i.i, i.j] = [estado.i,estado.j, i.fn]
                    fila.append(i)
                flag = False
                    
            fila.sort(key=operator.attrgetter('j'),reverse=True)
            fila.sort(key=operator.attrgetter('i'),reverse=True)
            fila.sort(key=operator.attrgetter('fn')) 
        
        if fila == []:
            print("Falhou")
            return 0
        estado = fila.pop(0)