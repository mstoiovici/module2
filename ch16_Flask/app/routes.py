from flask import Flask
app = Flask("MyApp")

@app.route("/")

def index():
    return "Hello World"

app.run(debug=True)
