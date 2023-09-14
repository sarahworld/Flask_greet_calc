from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# ***/welcome***   Returns “welcome”

# ***/welcome/home***   Returns “welcome home”

# ***/welcome/back***   Return “welcome back”

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/home")
def home():
    return "welcome home"

@app.route("/welcome/back")
def back():
    return "welcome back"