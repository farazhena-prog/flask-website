from flask import Flask

app = Flask(__name__)

@app.route("/hena")
def home():
    return "<h1>Hello Class</h1>"