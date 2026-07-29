

import requests
import pandas as pd


"""
url ="https://jsonplaceholder.typicode.com/users"

risposta = requests.get(url)

datiConvertiti = risposta.json()


tabellaDati = pd.DataFrame(datiConvertiti,columns=['id','name','username','email'])

print(tabellaDati)
print(type(tabellaDati))
"""

#due e più colonne sono un DataFrame
#una sola colonna è una Series

datiFile = pd.read_csv("FattureVirgola.csv",header=0,sep =',')
#print(datiFile)
#print(type(datiFile))

unasolaColonna = datiFile['nome']
#print(unasolaColonna)
#print(type(unasolaColonna))

datiFile['BuonFatturato'] = datiFile['Importo']>=3000

#datiFile['Test']="Digitare un valore"

datiFile['Ivato'] = datiFile['Importo'] + (datiFile['Importo']*22)/100

#funziona che calcola lo sconto (se soddisfa il criterio >2000)
def calcolaSconto(riga):
    if riga.Importo>2000:
        return riga.Importo - (riga.Importo*10)/100
    else:
        return riga.Importo

datiFile['Scontato'] = datiFile.apply(calcolaSconto,axis=1)
print(datiFile)

#struttura del dataframe
struttura = datiFile.shape
print(struttura)

print(datiFile.head())
print(datiFile.tail())

print("Raggruppamento: -----------------------------")
datiRaggruppati = datiFile.groupby(['cognome'])['Importo'].mean()
print(datiRaggruppati)


datiRaggruppati2 = datiFile.groupby(['cognome'])['Importo'].describe()
print(datiRaggruppati2)








print("Fine script")
