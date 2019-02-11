"""
Code authored by Matt Pregozen and Tim Horan
"""


from monopoly_game import Game

location = 'GO'
board_spaces = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2',
                'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'GTJ', 'G1',
                'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
dice_min_integer = 1
dice_max_integer = 4
cards_in_cc = ['GO', 'JAIL', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
cards_in_chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'Next R', 'Next R', 'Next U', 'Back 3',
                   'X', 'X', 'X', 'X', 'X', 'X']


game = Game(location, board_spaces, dice_min_integer, dice_max_integer, cards_in_cc, cards_in_chance)
print(len(board_spaces))


for i in range(0, 1000000):
    game.turn()

print(game.get_top_five())
print(game.get_top_five_strings())
print(game.get_top_five_prob())
print(game.get_length_visited())
