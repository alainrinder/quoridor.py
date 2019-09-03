#
# BuilderBot.py
#
# @author    Alain Rinder
# @date      2017.06.07-2019.09.04
# @version   0.1
#

import random
import time

from src.player.RandomBot import *
from src.action.IAction   import *
from src.exception.PlayerPathObstructedException import *



class BuilderBot(RandomBot):
    def computeFencePlacingImpacts(self, board):
        fencePlacingImpacts = {}
        # Compute impact of every valid fence placing
        for fencePlacing in board.storedValidFencePlacings:
            try:
                impact = board.getFencePlacingImpactOnPaths(fencePlacing)
            # Ignore path if it is blocking a player
            except PlayerPathObstructedException as e:
                continue
            globalImpact = 0
            for playerName in impact:
                globalImpact += (-1 if playerName == self.name else 1) * impact[playerName]
            fencePlacingImpacts[fencePlacing] = globalImpact
        return fencePlacingImpacts

    def getFencePlacingWithTheHighestImpact(self, fencePlacingImpacts):
        return max(fencePlacingImpacts, key = fencePlacingImpacts.get)

    def play(self, board) -> IAction:
        # If no fence left, move pawn
        if self.remainingFences() < 1 or len(board.storedValidFencePlacings) < 1:
            return self.moveRandomly(board)
        fencePlacingImpacts = self.computeFencePlacingImpacts(board)
        # If no valid fence placing, move pawn
        if len(fencePlacingImpacts) < 1:
            return self.moveRandomly(board)
        # Choose fence placing with the greatest impact
        bestFencePlacing = self.getFencePlacingWithTheHighestImpact(fencePlacingImpacts)
        # If impact is not positive, move pawn
        if fencePlacingImpacts[bestFencePlacing] < 1:
            return self.moveRandomly(board)
        return bestFencePlacing
