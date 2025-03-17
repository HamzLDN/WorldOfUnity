
from src.Base import Base
from users.Account import Account
from src.Player import Player
main_layout_base = {
    "level_1_walls":  (10, 6),
    "level_2_archer_tower": (8, 6)
}
another_one = {
    "level_1_walls": (5, 6)
}
saved_layouts = [
    main_layout_base,
    another_one,
]

if __name__ == '__main__':
    base = Base("Session", main_layout_base, saved_layouts)
    print(base.draw_layout())
    # username, password = ('Username', 'Password')
    # 
    # player.login()
    # print(player.loggedin)