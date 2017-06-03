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
    def __init__(self, board, coord):
        self.board = board
        self.coord = coord
        self.left    = (board.squareSize + board.innerSize)*coord.col
        self.xMiddle = self.left + int(board.squareSize/2)
        self.right   = self.left + board.squareSize
        self.top     = (board.squareSize + board.innerSize)*coord.row
        self.yMiddle = self.top + int(board.squareSize/2)
        self.bottom  = self.top + board.squareSize
        self.topLeft     = Point(self.left,    self.top)
        self.topRight    = Point(self.right,   self.top)
        self.bottomLeft  = Point(self.left,    self.bottom)
        self.bottomRight = Point(self.right,   self.bottom)
        self.middle      = Point(self.xMiddle, self.yMiddle)

    def draw(self, color = Color.SQUARE.value):
        if not INTERFACE:
            return 
        rectangle = Rectangle(self.topLeft, self.bottomRight)
        rectangle.setFill(color)
        rectangle.setWidth(0)
        rectangle.draw(self.board.window)