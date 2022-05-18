from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS,cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
socketio = SocketIO(app,ors_allowed_origins="http://localhost:3000")
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
# app.config['CORS_HEADERS'] = 'Content-Type'
# CORS(app)

@cross_origin()
@app.route('/')
def index():
    return {"data1":"hej från FLASK!"}

@cross_origin()
@socketio.on('connect')
def test_connect():
    print("Python connect")
    emit('after connect',  {'data':'Lets dance'})

if __name__ == '__main__':
    socketio.run(app, port="8000")