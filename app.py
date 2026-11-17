from flask import Flask, render_template
import random 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/o-meni")
def about():
    return render_template("about.html")

#met kocke.. random med 1 in 6
@app.route("/kocka")
def dice():
    return render_template("dice.html", kocka = random.randint(1,6))

#met kocke.. random med 1 in n
@app.route("/kocka/<N>")
def dice2(N):
    rnd=random.randint(1,int(N))
    print(rnd)
    return render_template("copy.html", kocka = rnd)

@app.route("/spol")
def spol():
    moski = ["Luka", "Marko", "Jan", "Žan", "Miha"]
    zenske = ["Ana", "Maja", "Eva", "Nika", "Lara"]

    ime_m = random.choice(moski)
    ime_z = random.choice(zenske)
    procent = random.randint(0, 100)

    return render_template("spol.html", ime_m=ime_m, ime_z=ime_z, procent=procent)


app.run(debug=True)