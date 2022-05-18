from flask import Flask
from flask_cors import CORS
#from flask import render_template


app = Flask(__name__)
CORS(app)

@app.route('/plot')
def build_plot():


    return "hej"

if __name__ == '__main__':
    app.debug = True
    app.run()