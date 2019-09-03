#
# BuildAndRunBot.py
#
# @author    Alain Rinder
# @date      2019.09.04
# @version   0.1
#

import random
import time

from src.player.BuilderBot import *
from src.player.RunnerBot  import *
from src.action.IAction    import *



class BuildAndRunBot(BuilderBot, RunnerBot):
    def play(self, board) -> IAction:
        # If no fence left, move pawn
        if self.remainingFences() < 1 or len(board.storedValidFencePlacings) < 1:
            return self.moveAlongTheShortestPath(board)
        fencePlacingImpacts = self.computeFencePlacingImpacts(board)
        # If no valid fence placing, move pawn
        if len(fencePlacingImpacts) < 1:
            return self.moveAlongTheShortestPath(board)
        # Choose fence placing with the greatest impact
        bestFencePlacing = self.getFencePlacingWithTheHighestImpact(fencePlacingImpacts)
        # If impact is not positive, move pawn
        if fencePlacingImpacts[bestFencePlacing] < 1:
            return self.moveAlongTheShortestPath(board)
        return bestFencePlacing
