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
from src.GridCoordinates     import *
from src.interface.Square    import *
from src.interface.Fence     import *
from src.action.PawnMove     import *
from src.action.FencePlacing import *



class Board(IDrawable):
    def __init__(self, game, cols, rows, squareSize, innerSize):
        self.game = game
        self.cols,       self.rows      = cols,       rows
        self.squareSize, self.innerSize = squareSize, innerSize
        self.grid = [[Square(self, GridCoordinates(col, row)) for row in range(rows)] for col in range(cols)] 
        self.width, self.height = squareSize*cols + innerSize*(cols - 1), squareSize*rows + innerSize*(rows - 1)
        if INTERFACE:
            self.window = GraphWin("Quoridor", self.width, self.height)
        self.pawns  = []
        self.fences = []
        self.firstCol  = 0
        self.middleCol = int((self.cols - 1)/2)
        self.lastCol   = self.cols - 1
        self.firstRow  = 0
        self.middleRow = int((self.rows - 1)/2)
        self.lastRow   = self.rows - 1

    def draw(self):
        if not INTERFACE:
            return 
        background = Rectangle(Point(0, 0), Point(self.width, self.height))
        background.setFill(Color.WHITE.value)
        background.setWidth(0)
        background.draw(self.window)
        for col in range(self.cols):
            for row in range(self.rows):
                self.grid[col][row].draw()
        #for player in self.game.players:
        #    player.pawn.draw()

    def startPosition(self, playerIndex) -> GridCoordinates:
        switcher = {
            0: GridCoordinates(self.middleCol, self.firstRow ),
            1: GridCoordinates(self.middleCol, self.lastRow  ),
            2: GridCoordinates(self.firstCol , self.middleRow),
            3: GridCoordinates(self.lastCol  , self.middleRow)
        }
        return switcher[playerIndex]

    def endPositions(self, playerIndex):
        colSwitcher = {
            0: None, 
            1: None, 
            2: self.lastCol, 
            3: self.firstCol 
        }
        rowSwitcher = {
            0: self.lastRow,
            1: self.firstRow,
            2: None,
            3: None
        }
        endCol, endRow = colSwitcher[playerIndex], rowSwitcher[playerIndex]
        endPositions = []
        if endCol is None and endRow is not None:
            for col in range(self.cols):
                endPositions.append(GridCoordinates(col, endRow))
        if endRow is None and endCol is not None:
            for row in range(self.rows):
                endPositions.append(GridCoordinates(endCol, row))
        return endPositions

    def getSquareAt(self, coord):
        return self.grid[coord.col][coord.row]

    def hasPawn(self, coord):
        for pawn in self.pawns:
            if pawn.coord == coord:
                return True
        return False

    def hasFenceAtLeft(self, coord):
        for fence in self.fences:
            if fence.direction == Fence.DIRECTION.VERTICAL and (fence.coord == coord or fence.coord == coord.top()):
                return True
        return False

    def hasFenceAtRight(self, coord):
        return self.hasFenceAtLeft(coord.right())

    def hasFenceAtTop(self, coord):
        for fence in self.fences:
            if fence.direction == Fence.DIRECTION.HORIZONTAL and (fence.coord == coord or fence.coord == coord.left()):
                return True
        return False

    def hasFenceAtBottom(self, coord):
        return self.hasFenceAtTop(coord.bottom())

    def isAtLeftEdge(self, coord):
        return (coord.col == self.firstCol)

    def isAtRightEdge(self, coord):
        return (coord.col == self.lastCol)

    def isAtTopEdge(self, coord):
        return (coord.row == self.firstRow)

    def isAtBottomEdge(self, coord):
        return (coord.row == self.lastRow)

    def validPawnMoves(self, coord):
        validMoves = []
        if not self.isAtLeftEdge(coord) and not self.hasFenceAtLeft(coord):
            leftCoord = coord.left()
            if not self.hasPawn(leftCoord):
                validMoves.append(PawnMove(coord, leftCoord))
            else:
                if not self.isAtLeftEdge(leftCoord) and not self.hasFenceAtLeft(leftCoord) and not self.hasPawn(leftCoord.left()):
                    validMoves.append(PawnMove(coord, leftCoord.left(), leftCoord))
                else:
                    if not self.isAtTopEdge(leftCoord) and not self.hasFenceAtTop(leftCoord) and not self.hasPawn(leftCoord.top()):
                        validMoves.append(PawnMove(coord, leftCoord.top(), leftCoord))
                    if not self.isAtBottomEdge(leftCoord) and not self.hasFenceAtBottom(leftCoord) and not self.hasPawn(leftCoord.bottom()):
                        validMoves.append(PawnMove(coord, leftCoord.bottom(), leftCoord))
        if not self.isAtRightEdge(coord) and not self.hasFenceAtRight(coord):
            rightCoord = coord.right()
            if not self.hasPawn(rightCoord):
                validMoves.append(PawnMove(coord, rightCoord))
            else:
                if not self.isAtRightEdge(rightCoord) and not self.hasFenceAtRight(rightCoord) and not self.hasPawn(rightCoord.right()):
                    validMoves.append(PawnMove(coord, rightCoord.right(), rightCoord))
                else:
                    if not self.isAtTopEdge(rightCoord) and not self.hasFenceAtTop(rightCoord) and not self.hasPawn(rightCoord.top()):
                        validMoves.append(PawnMove(coord, rightCoord.top(), rightCoord))
                    if not self.isAtBottomEdge(rightCoord) and not self.hasFenceAtBottom(rightCoord) and not self.hasPawn(rightCoord.bottom()):
                        validMoves.append(PawnMove(coord, rightCoord.bottom(), rightCoord))
        if not self.isAtTopEdge(coord) and not self.hasFenceAtTop(coord):
            topCoord = coord.top()
            if not self.hasPawn(topCoord):
                validMoves.append(PawnMove(coord, topCoord))
            else:
                if not self.isAtTopEdge(topCoord) and not self.hasFenceAtTop(topCoord) and not self.hasPawn(topCoord.top()):
                    validMoves.append(PawnMove(coord, topCoord.top(), topCoord))
                else:
                    if not self.isAtLeftEdge(topCoord) and not self.hasFenceAtLeft(topCoord) and not self.hasPawn(topCoord.left()):
                        validMoves.append(PawnMove(coord, topCoord.left(), topCoord))
                    if not self.isAtRightEdge(topCoord) and not self.hasFenceAtRight(topCoord) and not self.hasPawn(topCoord.right()):
                        validMoves.append(PawnMove(coord, topCoord.right(), topCoord))
        if not self.isAtBottomEdge(coord) and not self.hasFenceAtBottom(coord):
            bottomCoord = coord.bottom()
            if not self.hasPawn(bottomCoord):
                validMoves.append(PawnMove(coord, bottomCoord))
            else:
                if not self.isAtBottomEdge(bottomCoord) and not self.hasFenceAtBottom(bottomCoord) and not self.hasPawn(bottomCoord.bottom()):
                    validMoves.append(PawnMove(coord, bottomCoord.bottom(), bottomCoord))
                else:
                    if not self.isAtLeftEdge(bottomCoord) and not self.hasFenceAtLeft(bottomCoord) and not self.hasPawn(bottomCoord.left()):
                        validMoves.append(PawnMove(coord, bottomCoord.left(), bottomCoord))
                    if not self.isAtRightEdge(bottomCoord) and not self.hasFenceAtRight(bottomCoord) and not self.hasPawn(bottomCoord.right()):
                        validMoves.append(PawnMove(coord, bottomCoord.right(), bottomCoord))
        return validMoves

    def isValidPawnMove(self, fromCoord, toCoord, validMoves = None):
        if validMoves is None:
            validMoves = self.validPawnMoves(fromCoord)
        for validMove in validMoves:
            if validMove.toCoord == toCoord:
                return True
        return False

    def displayValidPawnMoves(self, player, validMoves = None):
        if validMoves is None:
            validMoves = self.validPawnMoves(player.pawn.coord)
        for validMove in validMoves:
            possiblePawn = Pawn(self, player)
            possiblePawn.coord = validMove.coord.clone()
            possiblePawn.draw(Color.Mix(player.color.value, Color.SQUARE.value))
            del possiblePawn

    def hideValidPawnMoves(self, player, validMoves = None):
        if validMoves is None: 
            validMoves = self.validPawnMoves(player.pawn.coord)
        for validMove in validMoves:
            possiblePawn = Pawn(self, player)
            possiblePawn.coord = validMove.coord.clone()
            possiblePawn.draw(Color.SQUARE.value, Color.SQUARE.value)
            del possiblePawn

    def validFencePlacings(self):
        validPlacings = []
        for col in range(self.cols):
            for row in range(self.rows):
                if (self.isValidFencePlacing(GridCoordinates(col, row), Fence.DIRECTION.HORIZONTAL)):
                    validPlacings.append(FencePlacing(GridCoordinates(col, row), Fence.DIRECTION.HORIZONTAL))
                if (self.isValidFencePlacing(GridCoordinates(col, row), Fence.DIRECTION.VERTICAL)):
                    validPlacings.append(FencePlacing(GridCoordinates(col, row), Fence.DIRECTION.VERTICAL))
        return validPlacings

    # TODO: check if it is blocking a player pawn
    def isValidFencePlacing(self, coord, direction):
        if not self.isAtTopEdge(coord) and not self.isAtRightEdge(coord) and direction == Fence.DIRECTION.HORIZONTAL and not self.hasFenceAtTop(coord) and not self.hasFenceAtTop(coord.right()):
            crossingFenceCoord = coord.top().right()
            for fence in self.fences:
                if fence.coord == crossingFenceCoord and fence.direction == Fence.DIRECTION.VERTICAL:
                    return False
            return True
        if not self.isAtLeftEdge(coord) and not self.isAtBottomEdge(coord) and direction == Fence.DIRECTION.VERTICAL and not self.hasFenceAtLeft(coord) and not self.hasFenceAtLeft(coord.bottom()):
            crossingFenceCoord = coord.bottom().left()
            for fence in self.fences:
                if fence.coord == crossingFenceCoord and fence.direction == Fence.DIRECTION.HORIZONTAL:
                    return False
            return True
        return False

    def displayValidFencePlacings(self, player, validPlacings = None):
        if validPlacings is None:
            validPlacings = self.validFencePlacings()
        for validPlacing in validPlacings:
            possibleFence = Fence(self, player)
            possibleFence.coord, possibleFence.direction = validPlacing.coord, validPlacing.direction
            possibleFence.draw(Color.Lighter(player.color.value))
            del possibleFence

    def hideValidFencePlacings(self, player, validPlacings = None):
        if validPlacings is None: 
            validPlacings = self.validFencePlacings()
        for validPlacing in validPlacings:
            possibleFence = Fence(self, player)
            possibleFence.coord, possibleFence.direction = validPlacing.coord, validPlacing.direction
            possibleFence.draw(Color.WHITE.value)
            del possibleFence

    def getSquareFromMousePosition(self, x, y):
        fullSize = self.squareSize + self.innerSize
        # on inner space
        if x % fullSize > self.squareSize or y % fullSize > self.squareSize:
            return None
        return self.grid[int(x/fullSize)][int(y/fullSize)]

    def getPawnMoveFromMousePosition(self, pawn, x, y) -> PawnMove:
        square = self.getSquareFromMousePosition(x, y)
        if square is None or not self.isValidPawnMove(pawn, square.coord):
            return None
        return PawnMove(pawn, square.coord)

    def getFencePlacingFromMousePosition(self, x, y) -> FencePlacing:
        fullSize = self.squareSize + self.innerSize
        # on square space
        if self.getSquareFromMousePosition(x, y) is not None:
            return None
        # vertical fence
        if x % fullSize > self.squareSize and y % fullSize < self.squareSize:
            square = self.getSquareFromMousePosition(x + self.squareSize, y)
            return FencePlacing(square.coord, Fence.DIRECTION.VERTICAL) if self.isValidFencePlacing(square.coord, Fence.DIRECTION.VERTICAL) else None
        # horizontal fence
        if x % fullSize < self.squareSize and y % fullSize > self.squareSize:
            square = self.getSquareFromMousePosition(x, y + self.squareSize)
            return FencePlacing(square.coord, Fence.DIRECTION.HORIZONTAL) if self.isValidFencePlacing(square.coord, Fence.DIRECTION.HORIZONTAL) else None
        # on inner crossing space
        if x % fullSize > self.squareSize and y % fullSize > self.squareSize:
            square = self.getSquareFromMousePosition(x + self.squareSize, y + self.squareSize)
            direction = Fence.DIRECTION.HORIZONTAL if square.left - x < square.top - y else Fence.DIRECTION.VERTICAL
            return FencePlacing(square.coord, direction) if self.isValidFencePlacing(square.coord, direction) else None
        return None


