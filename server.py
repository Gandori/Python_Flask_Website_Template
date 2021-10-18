from flask import Flask ,redirect ,url_for ,request
import os
from classes.config import DevelopmentConfig
from classes.Method_GET import Method_GET
from classes.Method_POST import Method_POST

def app():
    app = Flask(__name__)
    dir = os.path.dirname(os.path.abspath(__file__))
    app.template_folder = os.path.join(dir, "templates")
    app.static_folder = os.path.join(dir, "static")
    app.config.from_object(DevelopmentConfig())
    return app

def routes(app):
    @app.route("/" ,methods = ["GET"])
    def slash():
        return redirect(url_for("index"))


    @app.route("/index.html" ,methods = ["GET" ,"POST"])
    def index():

        if request.method == "POST": return Method_POST().POST
            
        if request.method == "GET": return Method_GET().GET

if __name__ == "__main__":
    app = app()
    routes(app)
    app.run(threaded = True)