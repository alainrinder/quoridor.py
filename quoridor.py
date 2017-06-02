
#
# quoridor.py
# 
# @author    Alain Rinder
# @date      2017.05.28-06.02
# @version   0.1
# @note      Python version: 3.6.1 [recommended] - 3.5.0 [minimal: https://docs.python.org/3/library/typing.html]
#
# TODO: 
#    use GridCoordinates class instead of col/row
# OK param graphical interface (disable draw functions...)
# OK split source files
#    handle exec params
#    check if fence placing will not block a player
#    create A* algorithm for path finding
#



import time
import random

from src.interface.Color  import *
from src.Game             import *
from src.player.Human     import *
from src.player.RandomBot import *



def main():
    game = Game([ # 2 or 4
        RandomBot("Alain",   Color.RED   ),
        RandomBot("Benoit",  Color.BLUE  ),
        RandomBot("Clément", Color.GREEN ),
        RandomBot("Daniel",  Color.ORANGE)
    ])
    game.start(5) # rounds
    game.end()


main()

