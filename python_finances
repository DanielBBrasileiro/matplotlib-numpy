# How to calculate return? 
#ret = (price(i) - price(i-1))/price(i-1)
# How to calculate with python and some data in a excel sheet?
         
import openpyxl 
import numpy as ny
import matplotlib.pyplot as fig

arq = openpyxl.load_workbook('/Users/daniel/Downloads/Exemplo_de_Acoes_1.1.xlsx')
plan= arq['Sheet1']
x=[cell for cell in next(plan.iter_cols(min_col=0, max_col=0, min_row=2, values_only=True))]

vetor=ny.array(x)
print(vetor)

retorno= (vetor[1:20] - vetor[0:19]/vetor[0:19])
print(retorno)

t=ny.arange(0,19)
fig.plot(t,retorno)

fig.title('Retorno')
fig.xlabel('tempo')
fig.ylabel('retorno')
