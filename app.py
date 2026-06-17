from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os
from predict import predict_email
from url_predict import predict_url as url_predictor

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Email model
email_model = joblib.load(os.path.join(BASE_DIR, 'model (1).pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'vectorizer (1).pkl'))

# URL model
url_model = joblib.load(os.path.join(BASE_DIR, 'url_model.pkl'))
url_columns = joblib.load(os.path.join(BASE_DIR, 'url_columns.pkl'))


@app.route('/predict_email', methods=['POST'])
def email_route():
    data = request.get_json()
    text = data['text']
    result = predict_email(text)
    return jsonify(result)


@app.route('/predict_url', methods=['POST'])
def url_route():
    data = request.get_json()
    url = data['url']
    result = url_predictor(url)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)