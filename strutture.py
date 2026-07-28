

#list (liste)
frutta =["Mela","Arancio","Susina",1500,False,[1500,600,520]]

print(type(frutta))


print("Numero di elementi nella lista:", len(frutta))

print(frutta[0])

frutta[1]="Melone"
print(frutta)

for fruit in frutta:
    print(fruit)

print(frutta[-1])


#aggiungi elementi alla lista
frutta.append('Cocomero')
print(frutta)

#ordinamento
#frutta.sort()
print(frutta)

nuovaFrutta =["Fragola","Kiwi","Ananas","Susina"]
frutta.extend(nuovaFrutta)
#frutta.append(nuovaFrutta)
print(frutta)

print(frutta[5][1])

print("Filtri di una lista")

def filtro(fruttaDaleggere):
    if fruttaDaleggere == "Susina":
        return True
    return False

filtrato = filter(filtro,frutta)  #restituisce SEMPRE un oggetto di tipo filter - Programmazione funzionale
print(type(filtrato))

print(list(filtrato))

#rimuovere
frutta.pop()
print(frutta)

frutta.remove("Susina")
print(frutta)


#tuple
print("Tupla --------------------------  IMMUTABILE sia nei VALORI che nella dimensione")
sport = ('Nuoto',"Tennis","Pallavolo")#,1500,True)
print(type(sport))
#sport.append("Calcio")

tuplaordinata = sorted(sport)
print(type(tuplaordinata))
print(tuplaordinata)

print(len(sport))

print(sport[0])

print("SET ----------------------------------")
citta ={'Milano',"Como","Pavia"}
print(type(citta))

citta.add("Pordenone")
print(citta)
citta.add("Como")
print(citta)

setOrdinato =sorted(citta)
print(type(setOrdinato))
print(setOrdinato)
print("Dictionary - JSON - -------------------------------")
persona ={"nome":'Mario Rossi',"anni":49}
print(type(persona))
print(persona)

print(persona['nome'])
persona['anni']=58
print(persona)

persona['citta'] ="Palermo"
print(persona)

chiavi = persona.keys()
print(type(chiavi))

for chiave in persona:
    print(chiave,"-", persona[chiave])


nuovaLista = list(chiavi)
print(nuovaLista)

nuovaSet=set(nuovaLista)
print(type(nuovaSet))

nuovaTupla=tuple(nuovaLista)
print(nuovaTupla)

"""
list  dinamica in ogni contesto (dimensione / valore)
tupla statica sia in dimensione che valore
set non accetta valori duplicati (non restituisce errore)
dictionary JSON   sono obbligatori i doppi apici nel nome della chiave

"""



