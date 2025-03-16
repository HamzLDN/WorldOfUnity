# from src.Player import Player
# from src.Base import Base
from users.Account import Account
from src.Player import Player
main_layout_base = {
    "level_1_walls": 5
}
another_one = {
    "level_1_walls": 5
}
saved_layouts = [
    main_layout_base,
    another_one,
]

if __name__ == '__main__':
    user = Player('Username', 'Password')
    user.register()
    user.get_username()