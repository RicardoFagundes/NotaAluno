# -*- coding: latin-1 -*-

'''
Created on 25 de nov. de 2021

@author: Ricardo Fagundes
'''
from Disciplina import Disciplina

arquivo = open("ArquivoCSV.csv", "r", encoding="utf8")

tamanho = arquivo.readlines()
cont = 0
lista_disciplinas = []

while(cont < len(tamanho)):

    if(cont == 0):
        cont += 1
        continue
 
    linha = tamanho[cont]
    vetor = linha.split(";")
    d = Disciplina()
    d.matricula = vetor[0]
    d.nome = vetor[1]
    d.nome_disciplina = vetor[2]
    d.nota1 = float(vetor[3])
    d.nota2 = float(vetor[4])
    d.nota3 = float(vetor[5])
    d.media = (d.nota1 + d.nota2 + d.nota3) / 2.0
    lista_disciplinas.append(d)
    cont += 1
arquivo.close()

for dados in lista_disciplinas:
    print("Nome da Discplina: " + dados.nome_disciplina)
    print("Nome do Aluno: " + dados.nome)
    print("Matricula: " + dados.matricula)
    if(dados.media >= 8.5):
        print("excelente: " + str(dados.media))
    elif (dados.media < 7.0 and  dados.media >= 8.5):
        print("bom : " + str(dados.media))
    else:
        print("preocupante : " + str(dados.media)) 
    print("******")