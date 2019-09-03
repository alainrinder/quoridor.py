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
    def moveRandomly(self, board) -> IAction:
        validPawnMoves = board.storedValidPawnMoves[self.pawn.coord] #board.validPawnMoves(self.pawn.coord)
        return random.choice(validPawnMoves)

    def placeFenceRandomly(self, board) -> IAction:
        randomFencePlacing = random.choice(board.storedValidFencePlacings)
        attempts = 5
        while board.isFencePlacingBlocking(randomFencePlacing) and attempts > 0:
            #print("Cannot place blocking %s" % randomFencePlacing)
            randomFencePlacing = random.choice(board.storedValidFencePlacings)
            attempts -= 1
        if (attempts == 0):
            return self.moveRandomly()
        return randomFencePlacing

    def play(self, board) -> IAction:
        # 1 chance over 3 to place a fence
        #validFencePlacings = board.validFencePlacings()
        if random.randint(0, 2) == 0 and self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0:
            return self.placeFenceRandomly(board)
        else:
            return self.moveRandomly(board)
