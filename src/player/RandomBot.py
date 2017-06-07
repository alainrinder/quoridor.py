#
# RandomBot.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

import random

from src.player.IBot    import *
from src.action.IAction import * 



class RandomBot(IBot):
    def play(self, board) -> IAction:
        # 1 chance over 3 to place a fence
        validFencePlacings = board.validFencePlacings()
        if random.randint(0, 2) == 0 and self.remainingFences() > 0 and len(validFencePlacings) > 0:
            return random.choice(validFencePlacings)
        else:
            validPawnMoves = board.validPawnMoves(self.pawn.coord)
            return random.choice(validPawnMoves)

