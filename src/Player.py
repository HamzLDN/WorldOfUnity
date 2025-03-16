from users.Account import Account

class Player(Account):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        self.__session = None

    def get_username(self):
        print(self.username)

    def view_friends(self):
        pass