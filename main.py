from src.Player import Player
from src.Base import Base

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
    base = Base(main_layout_base, saved_layouts)
    player = Player("Username", "Password")
