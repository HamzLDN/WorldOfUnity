from src.Player import Player

class Base(Player):
    def __init__(self, session, main_layout, saved_layouts, dimention=1200):
        self.main_layout = main_layout
        self.saved_layouts = saved_layouts
        self.dimention = dimention
        self.block_x_y = 100
        self.base = self.dimention/self.block_x_y # equals 12x12 (starts from top left)

    def get_main_layout(self):
        print("The layout '{}' belongs to {}".format(self.main_layout, _Player_get_username()))

    def get_saved_layout(self):
        return self.saved_layouts

    def draw_layout(self):
        print(self.main_layout)
        for asset in self.main_layout:
            print(asset, 'corresponds to', self.main_layout[asset])
            print(self.verify_square(self.main_layout[asset]))
        
    def verify_square(self, position):
        position = self.base*position[0]
        if position < 0: return False
        if position > self.dimention: return False
        return True
