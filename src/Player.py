

class Player:
    def __init__(self, username, password) -> None:
        self.username = username
        self.__password = password
        self.__session = None

    def login(self):
        print(self.__password)

    def get_username(self):
        return self.username

    def view_friends(self):
        pass