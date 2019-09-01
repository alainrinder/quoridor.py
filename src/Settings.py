#
# Settings.py
#
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

DEBUG     = True  # Display additionnal logs on console
INTERFACE = True  # Display window if true
TEMPO_SEC = 0.00  # Sleep time between each player, in seconds (default: 0)

TRACE = {
    "Path.BreadthFirstSearch": 0,
    "Path.Dijkstra": 0,
    "Board.validFencePlacings": 0,
    "Board.isValidFencePlacing": 0,
    "Board.validPawnMoves": 0,
    "Board.isValidPawnMove": 0,
    "Board.isFencePlacingBlocking": 0,
    "Board.getFencePlacingImpactOnPaths": 0,
    "Board.updateStoredValidActionsAfterPawnMove": 0,
    "Board.updateStoredValidActionsAfterFencePlacing": 0
}
