
from src.Base import Base
from users.Account import Account
from src.Player import Player
import numpy as np
import matplotlib.pyplot as plt

values = []
for i in range(100):
    values.append([i, 90])
# main_layout_base = {
#     "level_1_walls":  {"cord":[(0, 90), (10, 90), (20, 90), (30, 90), (40, 90), (50, 90)], "area": 1},
#     "arrow_tower":  {"cord":[(50, 50)], "area": 12},
# }
main_layout_base = {
    "walls":  {"cord":values, "area": 1},
    "eyes":  {"cord":[(25,20),(65, 20)], "area": 10},
    "nose":  {"cord":[(45,40)], "area": 10},
    "mouth":  {"cord":[(25,50),(35, 60),(45, 60), (55, 60), (65, 50)], "area": 10},
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