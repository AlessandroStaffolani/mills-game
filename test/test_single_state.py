from collections import namedtuple

from src.MillsGame import MillsGame
from core.algorithm.aima_alg import *
from src.game_utils import *

GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')

millsGame = MillsGame()

state_phase_one_error_double_game = GameState(to_move='W',
                                              utility=0,
                                              board=['B', 'W', 'O', 'W', 'O', 'O', 'W', 'W', 'W', 'O', 'W', 'O',
                                                     'W', 'O', 'B', 'B', 'B', 'O', 'O', 'W', 'O', 'B', 'O', 'B'],
                                              moves=[2, 4, 5, 13, 18, 20, 22, 9, 11], w_board=8, b_board=5,
                                              w_no_board=1,
                                              b_no_board=1)

state_phase_two = GameState(to_move='W',
                            utility=0,
                            board=['B', 'W', 'O', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'O',
                                   'W', 'O', 'B', 'B', 'B', 'W', 'B', 'W', 'O', 'O', 'O', 'B'],
                            moves=[2, 3, 5, 13, 20, 21, 22, 9, 11], w_board=9, b_board=5, w_no_board=0, b_no_board=0)

# TODO non funziona neanche cosi
state_phase_two_duoble_game = GameState(to_move='W',
                                        utility=0,
                                        board=['B', 'O', 'O', 'W', 'O', 'O', 'W', 'W', 'W', 'W', 'O', 'O',
                                               'W', 'O', 'B', 'B', 'B', 'W', 'W', 'W', 'O', 'B', 'O', 'B'],
                                        moves=[2, 4, 5, 13, 10, 20, 22, 1, 11], w_board=9, b_board=6, w_no_board=0,
                                        b_no_board=0)

state_phase_two_tris_trick = GameState(to_move='W',
                                       utility=0,
                                       board=['B', 'O', 'W', 'W', 'O', 'W', 'W', 'O', 'O', 'O', 'O', 'O',
                                              'O', 'W', 'B', 'B', 'B', 'O', 'W', 'W', 'W', 'B', 'W', 'B'],
                                       moves=[9, 4, 8, 12, 10, 17, 7, 1, 11], w_board=9, b_board=6, w_no_board=0,
                                       b_no_board=0)

# state_phase_two = GameState(to_move='W',
#                             utility=0,
#                             board=['B', 'B', 'O', 'B', 'W', 'B', 'O', 'B', 'O', 'W', 'W', 'O',  # l'ultima è la 11
#                                    'W', 'W', 'W', 'W', 'O', 'O', 'B', 'W', 'O', 'B', 'W', 'O'],
#                             moves=[2, 6, 8, 16, 17, 20, 23, 11], w_board=9, b_board=7, w_no_board=0, b_no_board=0)

state_phase_two_end = GameState(to_move='B',
                                utility=0,
                                board=['O', 'W', 'O', 'B', 'W', 'B', 'O', 'B', 'O', 'O', 'B', 'O',
                                       'W', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'B', 'B', 'O', 'B'],
                                moves=[0, 2, 8, 17, 9, 14, 6, 11, 22], w_board=8, b_board=7, w_no_board=0, b_no_board=0)

state_phase_three_start = GameState(to_move='B',
                                    utility=0,
                                    board=['O', 'W', 'O', 'B', 'W', 'B', 'O', 'O', 'O', 'O', 'O', 'O',
                                           'O', 'O', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'O', 'B'],
                                    moves=[0, 2, 8, 12, 10, 14, 6, 11, 22, 9, 21, 13, 7], w_board=8,
                                    b_board=3, w_no_board=0, b_no_board=0)

state_phase_three_test = GameState(to_move='B', utility=0, board=['O', 'W', 'O', 'W', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'W', 'O', 'O', 'B', 'B', 'W', 'W', 'O', 'O', 'W', 'O', 'O', 'B'], moves=[0, 4, 8, 12, 18, 5, 6, 2, 22, 9, 21, 13, 7, 19], w_board=7, b_board=3, w_no_board=0, b_no_board=0)



# millsGame.display(state_phase_three_start)
# print("State = " + str(state_phase_three_start))
# moves = millsGame.actions(state_phase_three_start)
# print("Moves = " + str(moves))

millsGame.display(state_phase_three_test)
print("State = " + str(state_phase_three_test))
moves = millsGame.actions(state_phase_three_test)
print("Moves = " + str(moves))





# print(check_couples_phase_two(state_phase_two_duoble_game, 18, 10, 'W'))