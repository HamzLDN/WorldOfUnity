from src.Player import Player
import numpy as np


class Base(Player):
    def __init__(self, session, main_layout, saved_layouts, dimention=1200):
        self.main_layout = main_layout
        self.saved_layouts = saved_layouts
        self.dimention = dimention # 1200x1200
        self.default_area = 12
        self.map = np.full((100, 100), ' ', dtype=object)
        self.grid = self.dimention/self.default_area
        np.set_printoptions(threshold=np.inf)

    def get_main_layout(self) -> None:
        print("The layout '{}' belongs to {}".format(self.main_layout, _Player_get_username()))

    def get_saved_layout(self) -> list:
        return self.saved_layouts

    def draw_layout(self) -> bool:
        print(self.main_layout)
        for asset in self.main_layout:
            print(asset, 'corresponds to', self.main_layout[asset])
            if not self.verify_square(self.main_layout[asset]['cord'], self.main_layout[asset]['area']):
                print(asset, 'failed to load. Position out of bounds.')
                return False
        return True


    def plot_land(self, position_x, position_y, area) -> bool:
        self.map[position_x:position_x + area, position_y:position_y + area] = '#'
        return True

    def verify_square(self, position, area) -> bool:
        
        position_y, position_x = position
        print("X and Y position: ",position_x, position_y)
        print("GRID IS ", self.grid)
        if position_x+area < 0 or position_y+area < 0: return False
        if position_x+area > self.grid or position_y+area > self.grid: return False
        print("DRAWING")
        return self.plot_land(position_x, position_y, area)