
class Account:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
