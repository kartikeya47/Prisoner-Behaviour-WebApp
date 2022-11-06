from flask import Flask, render_template, request, redirect
import os
import pickle
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        
        nature = request.form.get('nature')
        fight = request.form.get('fight')
        cook = request.form.get('cook')
        clean = request.form.get('clean')
        model = pickle.load(open('app/model', 'rb'))
        
        li = []
        
        if nature == 'Good':
            li.append(1)
            li.append(0)        
        if nature == 'Average':
            li.append(0)
            li.append(0)    
        if nature == 'Worst':
            li.append(0)
            li.append(1)
            
        if fight == 'Fights':
            li.append(0)
        if fight == 'Not Fights':
            li.append(1)
            
        if cook == 'No':
            li.append(0)
        if cook == 'Yes':
            li.append(1)
            
        if clean == 'No':
            li.append(0)
        if clean == 'Yes':
            li.append(1)
        
        listt = [li]
        result = model.predict(listt)
        
        res = 'str'
        
        if result[0] == 0:
            res = 'The Prisoner has Worst Behaviour'
        elif result[0] == 1:
            res = 'The Prisoner has Average Behaviour'
        elif result[0] == 2:
            res = 'The Prisoner has Good Behaviour'
        else:
            res = "Unknown Error"
    
    return render_template('output.html', result=res)