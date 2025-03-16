from src.Player import Player

class Base(Player):
    def __init__(self, session, main_layout, saved_layouts, dimention=1200):
        super().__init__(session)
        self.main_layout = main_layout
        self.saved_layouts = saved_layouts
        self.dimention = dimention
        self.base = self.dimention/100 # equals 12

    def get_main_layout(self):
        print("The layout '{}' belongs to {}".format(self.main_layout, _Player_get_username()))

    def get_saved_layout(self):
        return self.saved_layouts