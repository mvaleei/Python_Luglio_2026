

import matplotlib.pyplot as plt

import pandas as pd


datiFile = pd.read_csv("Fatturazionen1.csv", header = 0)

#print(datiFile)



y = datiFile['importo']
x = range(0,len(y))
plt.figure(figsize=(7,4))

plt.xlabel("Asse x = Numero fattura")
plt.ylabel("Asse y = Importo")

plt.grid()


plt.title("fatturato annuo")

plt.axhline(y = y.mean(), c="y" , linestyle ="dotted"   )



plt.plot(x,y)
plt.show()

