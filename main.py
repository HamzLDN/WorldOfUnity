
from src.Base import Base
from users.Account import Account
from src.Player import Player
import numpy as np
import matplotlib.pyplot as plt
main_layout_base = {
    "level_1_walls":  {"cord":(0, 91), "area": 10}
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
    output = base.draw_layout()
    if output:
        visual_map = np.where(base.map == '#', 1, 0).astype(np.uint8)
        plt.imshow(visual_map, cmap='gray', interpolation='nearest')
        plt.xticks([])
        plt.yticks([])
        plt.show()