

import requests
import pandas as pd



url ="https://jsonplaceholder.typicode.com/users"

risposta = requests.get(url)

datiConvertiti = risposta.json()


tabellaDati = pd.DataFrame(datiConvertiti,columns=['id','name','username','email'])

print(tabellaDati)

print("Fine script")
