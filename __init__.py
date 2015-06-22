from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/login")
def login():
    return "login page"

if __name__ == "__main__":
    app.run()
