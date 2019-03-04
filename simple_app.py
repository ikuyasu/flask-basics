from flask import Flask
from flask import render_template
# from flask import request

app = Flask(__name__)
print(__name__)
# __main__ or __simple_app__
# refers to yourself



# route
@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    return render_template('index.html', name=name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1':num1, 'num2':num2}
    return render_template('add.html', **context)
    # ('add.html', num1=num1, num2=num2)
    # to unpack the context

app.run(debug=True, port=8000, host='0.0.0.0')
