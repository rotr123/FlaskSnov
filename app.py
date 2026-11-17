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

sez=[1,2,4]
print(random.choice(sez))



app.run(debug=True)