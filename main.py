from flask import Flask, render_template
import datetime

import random
# print(year1)


app=Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(1, 10)
    date1 = datetime.datetime.now()
    year1 = date1.year
    return render_template("index.html", year=year1,num=random_num)
@app.route("/index.html")
def home1():
    return render_template("index.html")

@app.route("/generic.html")
def gen1():
    return render_template("generic.html")

@app.route("/elements.html")
def elements1():
    return render_template("elements.html")



if __name__=="__main__":
    app.run(debug=True)

