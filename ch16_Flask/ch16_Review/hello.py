from flask import Flask,render_template,request
app=Flask("MyApp")

@app.route("/")
def hello():
    return "I want to return something else"

@app.route("/Mariana")
def hello_someone():
    return "This will be Mariana's page"

@app.route("/Mariana/<name>")     ##### how do I return the else statement in my html, cause if I don't give a name, I'll get a not found URL error
def hello_someone_else(name):
    return render_template("hello.html", name=name.title())
######Get information from user

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print(form_data["email"])
    return "All OK"


app.run(debug=True,port=5001)
