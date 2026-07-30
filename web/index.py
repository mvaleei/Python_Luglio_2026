


from flask import Flask,render_template,jsonify,request

import mysql.connector

app =Flask(__name__)


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="Coletti_1",
    database ="pyluglio",
    use_pure=True
    )

miaconnessione=mydb.cursor()


#scrivo il codice delle chiamate ricevute dal client
@app.route("/")
def homemia():
    print("Mi hanno contattato mediante la home page")
    #return "Sono la home page del sito. Per ora solo testo"
    #return "<h1>Sono la home page del sito</h1>"
    return render_template("home.html")


@app.route("/inserisci")
def inserimento():
    return render_template("Inserisci.html")

@app.route("/pippo", methods=['POST'])
def registra():
    nominativocane= request.form['nomecane']
    razzacane =request.form['razzacane']
    annicane = request.form['annicane']
    #print(nominativocane,razzacane,annicane)
    datidaInviare =([nominativocane,razzacane,annicane])
    miaconnessione.callproc('nomestoredcreata',datidaInviare)
    mydb.commit()

    
    #ricerco l'ultimo cane inserito
    miaconnessione.execute("select * from cani where idcani = (select max(idcani) from cani)  ")
    dati = miaconnessione.fetchall()

    print(dati)

                            
    #print("Sono quasi pronto per registrare sul db")
    print("Ho registrato sul db")
    #return "registrerò"
    return render_template('Inserito.html',oggettofrontEnd = dati[0])


@app.route("/api/utenti",methods=['GET'])
def get_cani():
    miaconnessione.execute("select * from cani")
    dati = miaconnessione.fetchall()
    dati2 =[]
    #parsing dei dati ricevuti dal db
    for d in dati:
        dati2.append({"nome":d[1],"anni":d[2],"razza":d[3]})
        #print(type(d))
    #dati =[{"nome":"bobby","anni":5,"razza":"lupo"},{"nome":"kelly","anni":10,"razza":"barboncino"}]
    return dati2
    

@app.route("/api/utenti",methods=['POST'])
def post_cani():
    print(request.get_json())
    return request.get_json()

@app.route("/api/utenti",methods=['PUT'])
def put_cani():
    print(request.get_json())
    dati =[{"nome":"bobby","anni":5,"razza":"lupo"},{"nome":"kelly","anni":10,"razza":"barboncino"}]
    return jsonify(dati)


@app.route("/api/utenti",methods=['DELETE'])
def delete_cani():
    print(request.get_json())
    dati =[{"nome":"bobby","anni":5,"razza":"lupo"},{"nome":"kelly","anni":10,"razza":"barboncino"}]
    return jsonify(dati)

if __name__ == "__main__":
    app.run(port=5000)
