#
# Pawn.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from lib.graphics            import *

from src.interface.IDrawable import *
from src.interface.Color     import *



class Pawn(IDrawable):
    def __init__(self, board, player):
        self.board  = board
        self.player = player

    def draw(self, fillColor = None, textColor = Color.WHITE.value):
        if not INTERFACE:
            return 
        center = self.board.grid[self.col][self.row].middle
        radius = int(self.board.squareSize*0.4)
        circle = Circle(center, radius)
        circle.setFill(self.player.color.value if fillColor is None else fillColor)
        circle.setWidth(0)
        circle.draw(self.board.window)
        label = Text(center, self.player.name[:1])
        label.setSize(min(max(5, int(self.board.squareSize/2)), 36))
        #label.setStyle("bold")
        label.setTextColor(textColor)
        label.draw(self.board.window)

    def place(self, col, row):
        self.col = col
        self.row = row
        self.board.pawns.append(self)
        self.draw()

    def move(self, col, row):
        self.board.grid[self.col][self.row].draw()
        self.place(col, row)