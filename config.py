# size of the game board
WIDTH = 7
HEIGHT = 6

# characters for the game pieces
RED = "X"
BLACK = "O"
EMPTY = "."

# how many in a row needed to win
CONNECT_N = 4

# which heuristic function to call
HEURISTIC = "consecutive"
# HEURISTIC = "radius"


# radius heuristic constants
# how big the radius is for the radius heuristic
RADIUS = 2
SAME_COLOR_SCORE = 10
EMPTY_SQUARE_SCORE = 2
OPPONENT_COLOR_SCORE = -10
OPPONENT_VALUE = -0.7


# consecutive heuristic constants
MAX_SCORE = 100
THREE_SCORE = 20
TWO_SCORE = 5
OPPONENT_THREE_SCORE = -15
OPPONENT_TWO_SCORE = -3

