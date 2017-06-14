
#
# quoridor.py
# 
# @author    Alain Rinder
# @date      2017.05.28-06.02
# @version   0.1
# @note      Python version: 3.6.1 [recommended] - 3.5.0 [minimal: https://docs.python.org/3/library/typing.html]
#
# TODO: 
# OK Use GridCoordinates class instead of col/row
# OK Param graphical interface (disable draw functions...)
# OK Split source files
#    Handle exec params
# OK Check if fence placing will not block a player
# OK Create algorithms for path finding
#    BuilderBot: maximise other pawns path
# OK PERFORMANCE ISSUES: store valid fence placings, valid pawn moves with updates
# OK Check blocking fence using path without pawns (one path could exist but cannot be currently accessible because of a pawn) (DFS)
# OK Blocking fence checking failed on testing path with the future fence -> update valid pawn moves when appending fence in method isFencePlacingBlocking

from src.Settings          import *
from src.Game              import *
from src.player.Human      import *
from src.player.RandomBot  import *
from src.player.RunnerBot  import *
from src.player.BuilderBot import *



def main():
    """
    Main function of quoridor. 
    Create a game instance and launch game rounds.
    """
    game = Game([ # 2 or 4
        RunnerBot("Alain"),
        BuilderBot("Benoit"),
        BuilderBot("Clément"),
        BuilderBot("Daniel")
    ], totalFenceCount = 40)
    game.start(10) # rounds
    game.end()

    global TRACE
    print("TRACE")
    for i in TRACE:
    	print("%s: %s" % (i, TRACE[i]))

main()

