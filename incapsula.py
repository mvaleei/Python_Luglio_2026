

class fattura():
    __importo=0
    descrizione=""
    cliente=""

    def __init__(self, cliente,descrizione,importo):

        self.setImporto(importo)
            
        self.descrizione=descrizione
        self.cliente=cliente


    def dettagli(self):
        return self.cliente +"-" + self.descrizione+ "-" + str(self.__importo)

    def getImporto(self):
        return self.__importo

    def setImporto(self,nuovoImporto):
        if nuovoImporto<=5000:
            self.__importo=nuovoImporto
        else:
            self.__importo=5000

    @staticmethod
    def calcoloIva(importo,percentualeIva):
        return importo * percentualeIva/100
        
        


fat1 =fattura("Mario Rossi","Portatile",6000)

print(fat1.dettagli())


fat1.importo=6000
print(fat1.dettagli())


print(fat1.getImporto())

print(fattura.calcoloIva(8000,40))

