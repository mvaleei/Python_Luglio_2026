

class appartamento:
    mq=0
    citta=""
    indirizzo=""

    #costruttore
    def __init__(self, mqRicevuti,cittaRicevuta,IndirizzoRicevuto):
        self.mq=mqRicevuti
        self.citta=cittaRicevuta
        self.indirizzo = IndirizzoRicevuto

    #metodo/i
    def riepilogo(self):
        return self.citta + "-" + self.indirizzo + "-" + str(self.mq)

    def costoTotale(self,costomq):
        return costomq * self.mq



"""
viaRoma = appartamento()
vialePalermo =appartamento()
viaMontenapoleone=appartamento()


print(viaRoma)
print(vialePalermo)
print(viaMontenapoleone)

print(viaRoma.mq)
print(vialePalermo.mq)
print(viaMontenapoleone.mq)


viaRoma.mq=85
vialePalermo.mq=90
viaMontenapoleone.mq=60

print(viaRoma.mq)
print(vialePalermo.mq)
print(viaMontenapoleone.mq)

"""
viaRoma = appartamento (85,"Roma","Via Roma, 45")
vialePalermo =appartamento(90,"Palermo","Via Della Libertà")
viaMontenapoleone=appartamento(60,"Milano","Via Montenapoleone, 12")

"""
print(viaRoma.mq)
print(vialePalermo.mq)
print(viaMontenapoleone.mq)
"""
print(viaRoma.riepilogo())
print(vialePalermo.riepilogo())
print(viaMontenapoleone.riepilogo())

print(viaRoma.costoTotale(4500))
print(vialePalermo.costoTotale(5420))
print(viaMontenapoleone.costoTotale(10000))

class villa(appartamento):
    #mq=0
    #citta=""
    #indirizzo=""
    trattativa=""

    def __init__(self,mqvilla,cittavilla,indirizzovilla,trattativascelta):
        super().__init__(mqvilla,cittavilla,indirizzovilla)
        self.trattativa=trattativascelta

    def dettaglio(self):
        return self.riepilogo() + "-" + self.trattativa


eur =villa(220,'Roma','Viale Oceano Indiano, 1','Privata')
zen = villa(240,'Palermo','Viale Zen, 4',"Pubblica")
arcore = villa(180,"Milano","Piazza Fininvest","Privata")
#print(zen.riepilogo())
#print(eur.riepilogo())
#print(arcore.riepilogo())
print(zen.dettaglio())
print(eur.dettaglio())
print(arcore.dettaglio())

print(zen.costoTotale(4400))
print(eur.costoTotale(6400))
print(arcore.costoTotale(1200))
