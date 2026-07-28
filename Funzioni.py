
print("Funzione basica----------------")
def funzione1():
    print("Sono la tipologia di funzione che non necessita di input o output")

funzione1()






print("Funzione con parametro di ingresso---------------")
def funzione2(anni):
    if anni==18:
        print("Sei pronto per la patente")
    else:
        print("Devi ancora farti accompagnare")

funzione2(17)
funzione2(18)





print("Funzione con dao di ritorno------------")
def funzione3():
    #
    #
    #
    return "Funzione con dato di ritorno"

datoRitorno=funzione3()
print("Dalla funzione3 è tornato il seguente valore" , datoRitorno)



print("Funzione che riceve informazioni e ritorna dati--------------")
def funzione4(citta,anni):
    if citta =="Roma" and anni <18:
        return "Vivi nel Lazio e sei maggiorenne"
    else:
        return "Vivi in un'altra regione e non conosco i tuoi anni"

marioRossi=funzione4("Roma",15)
giorgioVerdi=funzione4("Firenze",26)

print(marioRossi)
print(giorgioVerdi)

print("Le funzioni che richiedono dei valori, si dice che SONO PROVVISTE DI FIRMA")

print("Fine dello script")


    
