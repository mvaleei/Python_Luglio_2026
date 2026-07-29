

#importiamo il modulo
import requests


#dichiariamo l'url da contattare
urlDaContattare ="https://jsonplaceholder.typicode.com/users"


#chiamata di tipo GET
chiamata = requests.get(urlDaContattare)

#print(type(chiamata))


#leggo i dati ed effettuo la deserializzazione
datiConvertiti = chiamata.json()
print(type(datiConvertiti))

for dato in datiConvertiti:
    #print(type(dato))
    print(dato['id'],dato['username'] )


print("Chiamata POST")
nuovo ={"id":666,"username":"Testmio","name":"pippo","email":"email@email.it"}

utenteInserito = requests.post(urlDaContattare,json=nuovo)
userNuovo=utenteInserito.json()
print(type(userNuovo))

print(userNuovo)



print("Fine dello script dei servizi")
