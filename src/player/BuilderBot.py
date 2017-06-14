#
# BuilderBot.py
# 
# @author    Alain Rinder
# @date      2017.06.07
# @version   0.1
#

import random
import time

from src.player.IBot    import *
from src.action.IAction import * 



class BuilderBot(IBot):
    def play(self, board) -> IAction:
        if self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0:
            randomFencePlacing = random.choice(board.storedValidFencePlacings)
            attempts = 5
            while board.isFencePlacingBlocking(randomFencePlacing) and attempts > 0:
                #print("Cannot place blocking %s" % randomFencePlacing)
                randomFencePlacing = random.choice(board.storedValidFencePlacings)
                attempts -= 1
            if (attempts == 0):
                validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
                return random.choice(validPawnMoves)
            return randomFencePlacing
        else:
            validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
            return random.choice(validPawnMoves)

