
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
# OK check if fence placing will not block a player
# OK create algorithms for path finding
#    BuilderBot
#    PERFORMANCE ISSUES: store valid fence placings, valid pawn moves (as a graph?) with updates
#

#from src.interface.Color   import *
from src.Settings          import *
from src.Game              import *
from src.player.Human      import *
from src.player.RandomBot  import *
from src.player.RunnerBot  import *
from src.player.BuilderBot import *



def main():
    game = Game([ # 2 or 4
        RunnerBot ("Alain"),
        BuilderBot("Benoit"),
        BuilderBot("Clément"),
        BuilderBot("Daniel")
    ], 9, 9, 40)
    game.start(1) # rounds
    game.end()

    global TRACE
    print("TRACE")
    for i in TRACE:
    	print("%s: %s" % (i, TRACE[i]))

main()

