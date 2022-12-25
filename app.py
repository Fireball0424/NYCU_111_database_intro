from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('final.html')

@app.route('/route_function', methods=['POST'])
def foo():
    json = request.json
    print('recv:', json)
    return json

if __name__ == '__main__':
    app.run(debug=True)
