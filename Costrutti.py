


#if
#anni=17

anni = int(input("Quanti anni hai:"))

if anni >17:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")


if anni<12:
    print("Sei un bambino")
elif anni>11 and anni <18:
    print("Sei un teen ager")
elif anni>17 and anni < 40:
    print("Sei adulto")
else:
    print("Sei troppo grande, vai in pensione")




#for
nome="Adalberto"

for carattere in nome:
    print(carattere)


numeroCaratteri =range(0,len(nome))

for numero in numeroCaratteri:
    print(numero, "-" , nome[numero])



#Se si esce dal ciclo con un break, non si esegue il blocco else
print("Ciclo con else")
for numero in numeroCaratteri:
    print(numero, "-" , nome[numero])
    if numero ==60:
        break
else:
    print("Sei uscito regolarmente da ciclo")


while nome=="Adalberto":
    print(nome)
    nome="Francesco"

    
