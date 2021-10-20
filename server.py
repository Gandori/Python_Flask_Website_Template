from flask import Flask ,redirect ,url_for ,request

from classes.method_post import method_post
from classes.method_get import method_get

class app:
    def __init__(self) -> None:
        self = Flask(__name__)

        @self.route("/<page>" ,methods = ["GET"])
        def other(page):
            return redirect(url_for("index"))

        @self.route("/" ,methods = ["GET"])
        def slash():
            
            return redirect(url_for("index"))

        @self.route("/index.html" ,methods = ["GET" ,"POST"])
        def index():

            if request.method == "POST": 
                return method_post().post

            if request.method == "GET":
                return method_get().get

        self.run(threaded = True ,debug=True)

if __name__ == "__main__":
    app()
