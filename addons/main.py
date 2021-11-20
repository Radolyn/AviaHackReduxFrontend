from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api/services')
def services():
    res = {
        'templates': [
            {
                'name': 'Сдать анализ на COVID-19'
            },
            {
                'name': 'Таможенное декларирование'
            }
        ]
    }
    
    return res

app.run(debug = True)