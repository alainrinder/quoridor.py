
#
# quoridor.py
# 
# @author    Alain Rinder
# @date      2017.05.28-06.02
# @version   0.1
# @note      Python version: 3.6.1 [recommended] - 3.5.0 [minimal: https://docs.python.org/3/library/typing.html]
#
# TODO: 
# OK use GridCoordinates class instead of col/row
# OK param graphical interface (disable draw functions...)
# OK split source files
#    handle exec params
#    check if fence placing will not block a player
#    create algorithms for path finding
#    move pawn.coord to player (pawn uses player's coord)
#    BuilderBot
#

#from src.interface.Color  import *
from src.Game             import *
from src.player.Human     import *
from src.player.RandomBot import *
from src.player.RunnerBot import *



def main():
    game = Game([ # 2 or 4
        RunnerBot("Alain"),
        RunnerBot("Benoit"),
        RunnerBot("Clément"),
        RunnerBot("Daniel")
    ])
    game.start(20) # rounds
    game.end()


main()

