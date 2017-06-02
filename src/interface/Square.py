#
# GridCoordinates.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from lib.graphics            import *

from src.interface.IDrawable import *
from src.interface.Color     import *



class Square(IDrawable):
    def __init__(self, board, col, row):
        self.board = board
        self.col = col
        self.row = row
        self.left    = (self.board.squareSize + self.board.innerSize)*self.col
        self.xMiddle = self.left + int(self.board.squareSize/2)
        self.right   = self.left + self.board.squareSize
        self.top     = (self.board.squareSize + self.board.innerSize)*self.row
        self.yMiddle = self.top + int(self.board.squareSize/2)
        self.bottom  = self.top + self.board.squareSize
        self.topLeft     = Point(self.left,    self.top)
        self.topRight    = Point(self.right,   self.top)
        self.bottomLeft  = Point(self.left,    self.bottom)
        self.bottomRight = Point(self.right,   self.bottom)
        self.middle      = Point(self.xMiddle, self.yMiddle)

    def draw(self, color = Color.SQUARE.value):
        if not INTERFACE:
            return 
        square = Rectangle(self.topLeft, self.bottomRight)
        square.setFill(color)
        square.setWidth(0)
        square.draw(self.board.window)