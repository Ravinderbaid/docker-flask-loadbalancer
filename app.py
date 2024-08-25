# app.py
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # ENV varibale for to export multiple port