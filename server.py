from flask import Flask ,redirect ,url_for ,request
import os
from config import DevelopmentConfig
from classes.Method_GET import Method_GET
from classes.Method_POST import Method_POST

app = Flask(__name__)
_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(_dir, "templates")
app.static_folder = os.path.join(_dir, "static")
app.config.from_object(DevelopmentConfig())

@app.route("/" ,methods = ["GET"])
def slash():
    print( app.config["SECRET_KEY"])
    return redirect(url_for("index"))


@app.route("/index.html" ,methods = ["GET" ,"POST"])
def index():

    if request.method == "POST":

        return Method_POST().POST
        
    elif request.method == "GET":

        return Method_GET().GET

if __name__ == "__main__":
    app.run(port="5000" ,threaded = True)