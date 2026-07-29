

#importiamo i moduli per effettuare lo scriping
import requests
from bs4 import BeautifulSoup


#leggo il contenuto della pagina
sitoweb = requests.get("https://www.inps.it/")

#print(sitoweb)

datihtml = BeautifulSoup(sitoweb.content,'html.parser')

#print(datihtml)

tagh2=datihtml.h2
#print(tagh2.text)


#tutti i tag di un certo tipo
tuttitagh2 = datihtml.find_all('h2')

for h2 in tuttitagh2:
    print(h2.text)


print("Ricerca per id")
perid = datihtml.find(id ="browserObsoletoLang")
print("Il contenuto del tag con id ObsoletoLang = ",perid.text)



print("Ricerca per le classi assegnati")
tagclasse = datihtml.find_all("a", class_ = 'nav-link')
print(len(tagclasse))

for tag in tagclasse:
    print(tag.text)

print("Fine dello script")
