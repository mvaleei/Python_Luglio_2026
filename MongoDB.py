

#importiamo il modulo per mongodb
import pymongo


#parametri di connessione
connessione = pymongo.MongoClient("mongodb://localhost:27017/")
database = connessione["pyluglio"]
collection = database["generica"]


#leggiamo i documents dalla collection
listato = collection.find()
#print(listato)


for documento in listato:
    ##print(documento)
    #print(type(documento))
    print(documento["_id"])




#scriviamo un document
nuovo = {"Qualifica":"Dirigente","etaLavoro":25,"Aziende":["Pippo srl","Minni snc","Pluto spa"]}
collection.insert_one(nuovo)


print("Fine script")
