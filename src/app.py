#'/api/v1/details'
#'/api/v1/healthz'

from flask import Flask, jsonify
import socket
import re
import datetime as dt

app = Flask(__name__)

def get_hostname():
    return socket.gethostname()

date = dt.datetime.now().strftime("%d-%m-%Y")
now = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
# convert to string
time = dt.datetime.now().strftime("%H:%M:%S")

@app.route('/api/v1/details')

def details():
    return jsonify(
        { 
            'date': date,
            'time': time,
            'hostname': get_hostname(),
            'message': 'GitHub/DockerHub mixed up'
        
        })

@app.route('/api/v1/healthz')

def health():
    return jsonify(
        { 'status': 'up'}),200


if __name__ == '__main__':

    app.run(host="0.0.0.0")    
