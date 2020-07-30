# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 14:09:37 2017

@author: Jones
"""
import pandas as pd

dados = pd.read_csv('restaurante.csv',header=None , delimiter=',')

amostra=dados.head(7)

amostra
amostra.to_csv('dados_amostra.csv')

transacoes = []
for i in range(0, 131):
    transacoes.append([str(dados.values[i, j]) for j in range(0, 16)])

    
from apyori import apriori
regras = apriori(transacoes, min_support=0.03, min_confidence=0.08, min_lift=3, min_lenght=2)

resultado = regras

i = 0

df = pd.DataFrame(columns=['Regra','Suporte','Confianca','Lift'])

for item in resultado:
    items = [x for x in item[0]]

   
    if items[0] != 'nan' and items[1] != 'nan':
        regra = ("Regra: " + items[0] + " -> " + items[1])
        suporte = format(item[1], '.2f')
        confianca = format(item[2][0][2], '.2f')
        lift =  format(item[2][0][3], '.2f')

        df.loc[i] = [regra, suporte,confianca,lift]
        
        i = i+1
    

print ("Foram geradas " + str(i) +" regras")

df.to_csv('regras.csv')
    

