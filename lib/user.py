class User:

    def __init__(self, name):
        print("User.__init__called.")
        self.name = name

    def log_in(self):
        self.logged_in = True
