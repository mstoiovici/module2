################Task1-build simple web app
"""
from flask import Flask
app=Flask(__name__)


@app.route("/")
def index():
    return "Hello World!!!!!!!!"

app.run(debug=True)
"""
###############Task2 - use routes and decorators
"""
from flask import Flask
app=Flask(__name__)


@app.route("/")
def index():
    return "Hello World!!!!!!!!"

@app.route("/Mariana")
def get_Mariana():
    return "This is Mariana's page!!!!!"

app.run(debug=True)
"""
###############Task3 - use render_template
"""
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World!! This is task3 - how two use render_template"


@app.route("/<name>")
def say_hello_to(name):
    return render_template("hello.html",title="hello", **locals())

app.run(debug=True)
"""
###############Task4 - use variables
"""
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    quote = "Mathematics is the key and door to the sciences. -- Galileo"
    return render_template("index.html",title="Mariana's Flask Project", **locals())



app.run(debug=True)
"""
###############Task5 - get email adress from user

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    quote = "Mathematics is the key and door to the sciences. -- Galileo"
    return render_template("index.html",title="Mariana's Flask Project", **locals())



@app.route("/confirmation", methods=["POST"])
def confirmation():
	form_data = request.form
    
	email = form_data["email"]
	result="All OK"
    type_form = type(form_data)
	return render_template("confirmation.html", title="Mariana's Form confirmation", **locals())

if __name__ == "__main__":
    app.run(debug=True)
