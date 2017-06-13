#
# BuilderBot.py
# 
# @author    Alain Rinder
# @date      2017.06.07
# @version   0.1
#

import random

from src.player.IBot    import *
from src.action.IAction import * 



class BuilderBot(IBot):
    def play(self, board) -> IAction:
        if self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0:
            randomFencePlacing = random.choice(board.storedValidFencePlacings)
            while board.isFencePlacingBlocking(randomFencePlacing):
                randomFencePlacing = random.choice(board.storedValidFencePlacings)
            return randomFencePlacing
        else:
            validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
            return random.choice(validPawnMoves)

