
class Account:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    @property
    def get_password(self):
        return self._password

    def register(self):
        print(f"{self.username} registered successfully with password {self._password}")

    def login(self):
        print(f"{self.username} logged in successfully with password {self._password}")