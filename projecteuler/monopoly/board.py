

class Board(object):
    """
    Board upon which a game is played
    """
    def __init__(self, spaces, start_location):
        self.spaces = spaces
        self.curr_location = start_location

    def move(self, num_spaces_to_move):
        board_length = len(self.spaces)
        next_location = (self.spaces.index(self.curr_location)+num_spaces_to_move) % board_length
        self.curr_location = self.spaces[next_location]

    def get_location(self):
        return self.curr_location

    def set_location(self, new_location):
        self.curr_location = new_location

    def go_to_next_x_space(self, space_type):
        for i in range(len(self.spaces)):
            self.move(1)
            if self.curr_location[0] == space_type:
                break


