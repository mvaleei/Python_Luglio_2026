


#pip install mysql-connector-python

#importo il modulo mysql
import mysql.connector



#configuro la connessione
mydb = mysql.connector.connect(
    host ='localhost',
    user='root',
    password ='Coletti_1',
    database ='pyluglio',
    use_pure=True
    )

miaconnessione = mydb.cursor()

#select
miaconnessione.execute('select * from cani')
datiletti = miaconnessione.fetchall()
print(len(datiletti))

for dog in datiletti:
    print(type(dog))
    print(dog)


#inserimento
stringaSQL = "insert into cani(nome,razza,anni) values ('laika','bassotto',1)"
miaconnessione.execute(stringaSQL)



#stored Procedure
datidaInviare =(['Lilly','Lupo',4])
miaconnessione.callproc('nomestoredcreata',datidaInviare)


mydb.commit()


print("Fine script")
