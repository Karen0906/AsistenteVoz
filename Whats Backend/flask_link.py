import numpy as np
import pickle
import pandas as pd

from flask import Flask, render_template, request

app = Flask(__name__)


def receive():
    resp = request.get_json().values()
    str_features = [str(x) for x in resp]
    Sex = str_features[0]
    return final_features

@app.route('/')
def home():
    return 'HOME'

@app.route('/BertQ&A',methods=['POST'])
def send():
    answer = receive()
    if answer == '':
        prediction = RF.predict(final_features)
        msgPred = 'Prediction for Survival is:\t\t' + ('Survived' if str(prediction[0]) =='1' else 'Dead') + '\nPrediction for Ticket class:\t' + str(final_features[0,0]) + '° class'
    answer = ''
    return msgPred

@app.route('/predictNN',methods=['POST'])
def predictNN():
    final_features = predictionPreparation()
    prediction = nn.predict(final_features)
    msgPred = 'Prediction for Survival is:\t\t' + ('Survived' if str(prediction[0]) =='1' else 'Dead') + '\nPrediction for Ticket class:\t' + str(final_features[0,0]) + '° class'
    return msgPred

if __name__ == "__main__":
    app.run('10.48.186.242')