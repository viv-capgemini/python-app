#'/api/v1/details'
#'/api/v1/healthz'

from flask import Flask, jsonify
import socket
import re
import datetime as dt

app = Flask(__name__)

def get_hostname():
    return socket.gethostname()

now = dt.datetime.now().strftime("%d-%m-%Y")

@app.route('/api/v1/details')

def details():
    return jsonify(
        { 
            'date': now,
            'hostname': get_hostname()
        
        })

@app.route('/api/v1/healthz')

def health():
    return jsonify(
        { 'status': 'up'}),200


if __name__ == '__main__':

    app.run(host="0.0.0.0")    