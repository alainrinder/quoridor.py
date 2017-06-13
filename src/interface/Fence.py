#
# Fence.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from lib.graphics            import *

from src.interface.IDrawable import *
from src.interface.Color     import *



class Fence(IDrawable):
    class DIRECTION(Enum):
        HORIZONTAL = 0
        VERTICAL   = 1

    def __init__(self, board, player):
        self.board  = board
        self.player = player

    def draw(self, color = None):
        if not INTERFACE:
            return 
        square = self.getSquare()
        rectangleLength = 2*self.board.squareSize + self.board.innerSize
        rectangleWidth  = self.board.innerSize
        if (self.direction == Fence.DIRECTION.HORIZONTAL):
            rectangle = Rectangle(Point(square.left, square.top - rectangleWidth), Point(square.left + rectangleLength, square.top))
        else: 
            rectangle = Rectangle(Point(square.left - rectangleWidth, square.top), Point(square.left, square.top + rectangleLength))
        rectangle.setFill(self.player.color.value if color is None else color)
        rectangle.setWidth(0)
        rectangle.draw(self.board.window)

    def place(self, coord, direction):
        self.coord = coord
        self.direction = direction
        self.board.fences.append(self)
        self.board.updateStoredValidActionsAfterFencePlacing(coord, direction)
        self.draw()

    def getSquare(self):
        return self.board.getSquareAt(self.coord)

    def __str__(self):
        vertical = (self.direction == Fence.DIRECTION.VERTICAL)
        return "%s-fence at %s" % ("V" if vertical else "H", self.coord)


