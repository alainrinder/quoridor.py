#
# IPlayer.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.action.IAction import * 



class IPlayer:
    def __init__(self, name, color):
        self.name   = name
        self.color  = color
        self.pawn   = None
        self.fences = []
        self.score  = 0

    def play(self, board) -> IAction:
        pass

    def movePawn(self, col, row):
        self.pawn.move(col, row)

    def placeFence(self, col, row, direction):
        fence = self.fences.pop()
        fence.place(col, row, direction)

    def remainingFences(self):
        return len(self.fences)

    def __str__(self):
        return "%s (%s)" % (self.name, self.color.name)


