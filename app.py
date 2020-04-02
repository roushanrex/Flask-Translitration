from flask import Flask, render_template, request
from sklearn.externals import joblib
import pandas as pd
import numpy as np
from indictrans import Transliterator
import ast



app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/predict", methods = ['POST', "GET"])
def predict():
    
    if request.method == 'POST':
        print(request.form.get('NewYork'))
        try:

            NewYork = request.form['NewYork']
            California = request.form['California']
            Florida = request.form['Florida']
            NewYorkstrip = NewYork.strip()
            NewYorkLower = NewYorkstrip.lower()
  
            f = open("data/Alldata.csv", "r")
            s = f.read()
            dic = ast.literal_eval(s)
            my_list = []
            words = NewYorkLower.split() 
            
            for c in words:
                trn = Transliterator(source=California.strip(), target=Florida.strip(), build_lookup=True)
                eng = trn.transform(c.lower())
                my_list.append(dic.get(c,eng)) 
                a = my_list
                
            listToStr = ' '.join(map(str, a)) 
            

        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('home.html', prediction = listToStr)

if __name__ == "__main__":
    app.run()