#
# RunnerBot.py
# 
# @author    Alain Rinder
# @date      2017.06.07
# @version   0.1
#

from src.player.IBot    import *
from src.action.IAction import * 
from src.Path           import *



class RunnerBot(IBot):
    def play(self, board) -> IAction:
        path = Path.BreadthFirstSearch(board, self.pawn.coord, self.endPositions, ignorePawns = False)
        if path is None:
            path = Path.BreadthFirstSearch(board, self.pawn.coord, self.endPositions, ignorePawns = True)
            firstMove = path.firstMove()
            if not board.isValidPawnMove(firstMove.fromCoord, firstMove.toCoord, ignorePawns = False):
                #board.drawOnConsole()
                return None
        return path.firstMove()

