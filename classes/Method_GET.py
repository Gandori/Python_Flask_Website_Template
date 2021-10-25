from flask import render_template

class method_get:
    def __init__(self) -> None:
        
        def get():
            return render_template(self.page)

        self.page = "index.html"
        self.get = get()
