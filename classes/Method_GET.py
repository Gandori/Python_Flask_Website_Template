from classes.render import render

class method_get:
    def __init__(self) -> None:
        
        def get():
            return render().render

        self.get = get()
