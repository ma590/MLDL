import json
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from flask_cors import CORS, cross_origin
import numpy as np

# Charger les paramètres depuis le fichier JSON
with open('config.json', 'r') as config_file:
    params = json.load(config_file)

# Utiliser les paramètres
seq_length = params['seq_length']



app = Flask(__name__)
CORS(app)  # ou bien cors = CORS(app)

model = load_model('time_series_model.h5')

@app.route('/predict', methods=['POST'])
@cross_origin()  # Utilisez le décorateur cross_origin
def predictions():
    data = request.json['data']
    data = np.array(data).reshape(-1, seq_length-1, 1)
    prediction = model.predict(data)
    return jsonify({'predict': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
