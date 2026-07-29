


from flask import Flask,render_template,request

app =Flask(__name__)


#scrivo il codice delle chiamate ricevute dal client
@app.route("/")
def homemia():
    print("Mi hanno contattato mediante la home page")
    #return "Sono la home page del sito. Per ora solo testo"
    #return "<h1>Sono la home page del sito</h1>"
    return render_template("home.html")



if __name__ == "__main__":
    app.run(port=5000)
