from flask import Flask




app = Flask(__name__)


# http://localhost:5000/
@app.route("/", methods=['GET'])
def index():
    return "<h1>Hello, World!</h1>"



# http://localhost:5000/sayhello/<name>
@app.route("/sayhello/<name>", methods=['GET'])
def say_hello(name):
    return f"<h1>hello {name}!</h1>"





# http://localhost:5000/add/<num1>/<num2>
@app.route("/add/<int:num1>/<int:num2>", methods=['GET'])
def add(num1, num2):

    return f"<h1>result: {num1 + num2}!</h1>"


# http://localhost:5000/add/<num1>/<num2>
@app.route("/sub/<int:num1>/<int:num2>", methods=['GET'])
def sub(num1, num2):

    return f"<h1>result: {num1 - num2}!</h1>"










app.run('127.0.0.1', 5000, debug=True)