class Members(Player):
    def __init__(self, players_username, suggested_players, friends_list):
        self.players_username = players_username: list
        self.suggested_players = suggested_players: list
        self.friends_list = friends_list: list

    def add_username(self, username) -> bool:
        print("ADD USERNAME:", username)

    def view_suggested_players(self) -> list:
        pass

    def view_friend_list(self) -> list:
        pass
