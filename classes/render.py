from flask import render_template

class render:
    def __init__(self) -> None:

        def render_page():
            return render_template(self.page)

        self.page = "index.html"
        self.render = render_page()