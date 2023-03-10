from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import jsonify

from database import Database
from plot import Plot

app = Flask(__name__)
database = Database()
plot = Plot()


@app.route('/')
def index():
    print('blalala')
    return render_template('query.html')

@app.route('/route_function', methods=['POST', 'GET'])
def success():
    if request.method == 'POST' : 
        json_file = request.json
        result = database.GetJobWithMultipleSkillsProMax(json_file)
        
        plot.drawJobTitle(data=result)
        plot.drawLocation(data=result)
        plot.drawSalary(data=result)
        
        return render_template('res2.html', value=result)

    else :
        return render_template('query.html')

@app.route('/test', methods=['POST'])
def foo():
    return render_template('query.html')

if __name__ == '__main__':
    app.run(debug=False)