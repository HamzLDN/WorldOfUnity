from src.Player import Player
import numpy as np


class Base(Player):
    def __init__(self, session, main_layout, saved_layouts, dimention=1200):
        self.main_layout = main_layout
        self.saved_layouts = saved_layouts
        self.dimention = dimention
        self.default_area = 12
        self.map = np.full((100, 100), '', dtype=object)
        np.set_printoptions(threshold=np.inf)
    def get_main_layout(self):
        print("The layout '{}' belongs to {}".format(self.main_layout, _Player_get_username()))

    def get_saved_layout(self):
        return self.saved_layouts

    def draw_layout(self):
        print(self.main_layout)
        for asset in self.main_layout:
            print(asset, 'corresponds to', self.main_layout[asset])
            print(self.verify_square(self.main_layout[asset]['cord'], self.main_layout[asset]['area']))

    def plot_land(self, position_x, position_y, area):
        print(type(position_x), type(position_y))
        for x in range(area):
            for y in range(area):
                self.map[x, y] = '#'

    def verify_square(self, position, area):
        self.base = self.dimention/self.default_area
        position_x, position_y = position

        position_x+=area
        position_y+=area
        print(position_x, position_y, self.base)
        if position_x < 0 and position_y < 0: return False
        if position_x > self.base and position_y > self.base: return False
        return self.plot_land(position_x, position_y, area)

