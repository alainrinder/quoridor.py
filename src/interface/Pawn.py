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
        self.coord  = None

    def draw(self, fillColor = None, textColor = Color.WHITE.value):
        if not INTERFACE:
            return 
        center = self.getSquare().middle
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

    def place(self, coord):
        fromCoord, toCoord = None if self.coord is None else self.coord.clone(), coord
        self.coord = coord
        self.board.pawns.append(self)
        self.board.updateStoredValidActionsAfterPawnMove(fromCoord, toCoord)
        self.draw()

    def move(self, coord):
        self.getSquare().draw()
        self.place(coord)

    def getSquare(self):
        return self.board.getSquareAt(self.coord)


