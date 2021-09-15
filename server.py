from flask import Flask ,redirect ,url_for ,request
import os

from classes.Method_GET import Method_GET
from classes.Method_POST import Method_POST

# dir
app = Flask(__name__)
_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(_dir, "templates")
app.static_folder = os.path.join(_dir, "static")
app.debug = True

# Session
Key = "test"
app.secret_key = Key


@app.route("/" ,methods = ["GET"])
def slash():
 
    return redirect(url_for("index"))


@app.route("/index.html" ,methods = ["GET" ,"POST"])
def index():

    if request.method == "POST":

        return Method_POST().POST
        
    elif request.method == "GET":

        return Method_GET().GET


app.run(host="localhost" ,port="1000" ,threaded = True)