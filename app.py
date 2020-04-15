import pandas as pd
from flask import Flask, request, render_template

from functions import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def render_classifier():
    return render_template('classifier.html')

@app.route('/', methods = ['POST'])
def predict():
    text = request.form.get('text')
    prediction = get_rec(text)
    if prediction == None:
        return render_template('nope.html', variable = prediction)
    if prediction != None:
        return render_template('twss.html', v = text, variable = prediction)


if __name__ == '__main__':
    app.run()
