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
            fencePlacingImpacts = {}
            for fencePlacing in board.storedValidFencePlacings:
                print(fencePlacing)
                impact = board.getFencePlacingImpactOnPaths(fencePlacing)
                if impact is None:
                    continue
                globalImpact = 0
                for playerName in impact:
                    globalImpact += (-1 if playerName == self.name else 1) * impact[playerName]
                print(globalImpact)
                fencePlacingImpacts[fencePlacing] = globalImpact
            if len(fencePlacingImpacts) == 0:
                #print ("No valid fence placing!")
                validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
                return random.choice(validPawnMoves)
            bestFencePlacing = max(fencePlacingImpacts, key = fencePlacingImpacts.get)
            if fencePlacingImpacts[bestFencePlacing] == 0:
                #print ("No positive impact when placing fence")
                validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
                return random.choice(validPawnMoves)
            return bestFencePlacing
        else:
            validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
            return random.choice(validPawnMoves)
