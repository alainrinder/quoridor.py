
#
# quoridor.py
#
# @author    Alain Rinder
# @date      2017.06.01 - 2019-09-01
# @version   0.1
# @note      Python version: 3.6.1 [recommended] - 3.5.0 [minimal: https://docs.python.org/3/library/typing.html]
#
# TODO:
# OK Use GridCoordinates class instead of col/row
# OK Param graphical interface (disable draw functions...)
# OK Split source files
# OK Handle exec params
# OK Check if fence placing will not block a player
# OK Create algorithms for path finding
# OK BuilderBot: maximise other pawns path
# OK PERFORMANCE ISSUES: store valid fence placings, valid pawn moves with updates
# OK Check blocking fence using path without pawns (one path could exist but cannot be currently accessible because of a pawn) (DFS)
# OK Blocking fence checking failed on testing path with the future fence -> update valid pawn moves when appending fence in method isFencePlacingBlocking
#    Create a bot combining BuilderBot & RunnerBot (run if path is shorter)
# OK Fix path bug (sometimes consider a player as blocked, but paths still exist)

import getopt

from src.Settings              import *
from src.Game                  import *
from src.player.Human          import *
from src.player.RandomBot      import *
from src.player.RunnerBot      import *
from src.player.BuilderBot     import *
from src.player.BuildAndRunBot import *


PARAMETERS_ERROR_RETURN_CODE = 1

def printUsage():
    print("Usage: python quoridor.py [{-h|--help}] {-p|--players=}<PlayerName:PlayerType,...> [{-r|--rounds=}<roundCount>] [{-x|--cols=}<ColCount>] [{-y|--rows=}<RowCount>] [{-f|--fences=}<TotalFenceCount>] [{s|--square_size=}<SquareSizeInPixels>]")
    print("Example: python quoridor.py --players=Alain:Human,Benoit:BuilderBot,Caroline:RandomBot,Daniel:RunnerBot --square-size=32")

def readArguments():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:r:w:x:y:s:h", ["players=", "rounds=", "cols=", "rows=", "fences=", "square_size=", "help"])
    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(PARAMETERS_ERROR_RETURN_CODE)
    players = []
    rounds = 1
    cols = 9
    rows = 9
    totalFenceCount = 20
    squareSize = 32
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit(0)
        elif opt in ("-p", "--players"):
            for playerData in arg.split(","):
                playerName, playerType = playerData.split(":")
                if playerType not in globals():
                    print("Unknown player type %s . Abort." % (playerType))
                    sys.exit(PARAMETERS_ERROR_RETURN_CODE)
                players.append(globals()[playerType](playerName))
            if len(players) not in (2, 4):
                print("Expect 2 or 4 players. Abort.")
                sys.exit(PARAMETERS_ERROR_RETURN_CODE)
        elif opt in ("-r", "--rounds"):
            rounds = int(arg)
        elif opt in ("-x", "--cols"):
            cols = int(arg)
        elif opt in ("-y", "--rows"):
            rows = int(arg)
        elif opt in ("-f", "--fences"):
            totalFenceCount = int(arg)
        elif opt in ("-s", "--square_size"):
            squareSize = int(arg)
        else:
            print("Unhandeld option. Abort.")
            sys.exit(PARAMETERS_ERROR_RETURN_CODE)
    return players, rounds, cols, rows, totalFenceCount, squareSize

def main():
    """
    Main function of quoridor.
    Create a game instance and launch game rounds.
    """
    players, rounds, cols, rows, totalFenceCount, squareSize = readArguments()

    game = Game(players, cols, rows, totalFenceCount, squareSize)
    game.start(rounds)
    game.end()

    global TRACE
    print("TRACE")
    for i in TRACE:
    	print("%s: %s" % (i, TRACE[i]))

main()
