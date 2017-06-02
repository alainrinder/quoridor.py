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
        self.grid = [[Square(self, col, row) for row in range(rows)] for col in range(cols)] 
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
        for player in self.game.players:
            player.pawn.draw()

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

    def hasPawn(self, col, row):
        for pawn in self.pawns:
            if (pawn.col == col and pawn.row == row):
                return True
        return False

    def hasFenceAtLeft(self, col, row):
        for fence in self.fences:
            if ((fence.direction == Fence.DIRECTION.VERTICAL and fence.col == col) and (fence.row == row or fence.row == row - 1)):
                return True
        return False

    def hasFenceAtRight(self, col, row):
        for fence in self.fences:
            if ((fence.direction == Fence.DIRECTION.VERTICAL and fence.col == col + 1) and (fence.row == row or fence.row == row - 1)):
                return True
        return False

    def hasFenceAtTop(self, col, row):
        for fence in self.fences:
            if ((fence.direction == Fence.DIRECTION.HORIZONTAL and fence.row == row) and (fence.col == col or fence.col == col - 1)):
                return True
        return False

    def hasFenceAtBottom(self, col, row):
        for fence in self.fences:
            if ((fence.direction == Fence.DIRECTION.HORIZONTAL and fence.row == row + 1) and (fence.col == col or fence.col == col - 1)):
                return True
        return False

    def validPawnMoves(self, pawn):
        validMoves = []
        col, row = pawn.col, pawn.row
        if col >= 1 and not self.hasFenceAtLeft(col, row):
            if not self.hasPawn(col - 1, row):
                validMoves.append(PawnMove(pawn, col - 1, row))
            else:
                if col >= 2 and not self.hasFenceAtLeft(col - 1, row) and not self.hasPawn(col - 2, row):
                    validMoves.append(PawnMove(pawn, col - 2, row))
                else:
                    if row >= 1 and not self.hasFenceAtTop(col - 1, row) and not self.hasPawn(col - 1, row - 1):
                        validMoves.append(PawnMove(pawn, col - 1, row - 1))
                    if row <= self.rows - 2 and not self.hasFenceAtBottom(col - 1, row) and not self.hasPawn(col - 1, row + 1):
                        validMoves.append(PawnMove(pawn, col - 1, row + 1))
        if col <= self.cols - 2 and not self.hasFenceAtRight(col, row):
            if not self.hasPawn(col + 1, row):
                validMoves.append(PawnMove(pawn, col + 1, row))
            else:
                if col <= self.cols - 3 and not self.hasFenceAtRight(col + 1, row) and not self.hasPawn(col + 2, row):
                    validMoves.append(PawnMove(pawn, col + 2, row))
                else:
                    if row >= 1 and not self.hasFenceAtTop(col + 1, row) and not self.hasPawn(col + 1, row - 1):
                        validMoves.append(PawnMove(pawn, col + 1, row - 1))
                    if row <= self.rows - 2 and not self.hasFenceAtBottom(col + 1, row) and not self.hasPawn(col + 1, row + 1):
                        validMoves.append(PawnMove(pawn, col + 1, row + 1))
        if row >= 1 and not self.hasFenceAtTop(col, row):
            if not self.hasPawn(col, row - 1):
                validMoves.append(PawnMove(pawn, col, row - 1))
            else:
                if row >= 2 and not self.hasFenceAtTop(col, row - 1) and not self.hasPawn(col, row - 2):
                    validMoves.append(PawnMove(pawn, col, row - 2))
                else:
                    if col >= 1 and not self.hasFenceAtLeft(col, row - 1) and not self.hasPawn(col - 1, row - 1):
                        validMoves.append(PawnMove(pawn, col - 1, row - 1))
                    if col <= self.cols - 2 and not self.hasFenceAtRight(col, row - 1) and not self.hasPawn(col + 1, row - 1):
                        validMoves.append(PawnMove(pawn, col + 1, row - 1))
        if row <= self.rows - 2 and not self.hasFenceAtBottom(col, row):
            if not self.hasPawn(col, row + 1):
                validMoves.append(PawnMove(pawn, col, row + 1))
            else:
                if row <= self.rows - 3 and not self.hasFenceAtBottom(col, row + 1) and not self.hasPawn(col, row + 2):
                    validMoves.append(PawnMove(pawn, col, row + 2))
                else:
                    if col >= 1 and not self.hasFenceAtLeft(col, row + 1) and not self.hasPawn(col - 1, row + 1):
                        validMoves.append(PawnMove(pawn, col - 1, row + 1))
                    if col <= self.cols - 2 and not self.hasFenceAtRight(col, row + 1) and not self.hasPawn(col + 1, row + 1):
                        validMoves.append(PawnMove(pawn, col + 1, row + 1))
        return validMoves

    def isValidPawnMove(self, pawn, col, row, validMoves = None):
        if validMoves is None:
            validMoves = self.validPawnMoves(pawn)
        for validMove in validMoves:
            if (validMove.col == col and validMove.row == row):
                return True
        return False

    def displayValidPawnMoves(self, player, validMoves = None):
        if validMoves is None:
            validMoves = self.validPawnMoves(player.pawn)
        for validMove in validMoves:
            possiblePawn = Pawn(self, player)
            possiblePawn.col, possiblePawn.row = validMove.col, validMove.row
            possiblePawn.draw(Color.Mix(player.color.value, Color.SQUARE.value))
            del possiblePawn

    def hideValidPawnMoves(self, player, validMoves = None):
        if validMoves is None: 
            validMoves = self.validPawnMoves(player.pawn)
        for validMove in validMoves:
            possiblePawn = Pawn(self, player)
            possiblePawn.col, possiblePawn.row = validMove.col, validMove.row
            possiblePawn.draw(Color.SQUARE.value, Color.SQUARE.value)
            del possiblePawn

    def validFencePlacings(self):
        validPlacings = []
        for col in range(self.cols):
            for row in range(self.rows):
                if (self.isValidFencePlacing(col, row, Fence.DIRECTION.HORIZONTAL)):
                    validPlacings.append(FencePlacing(col, row, Fence.DIRECTION.HORIZONTAL))
                if (self.isValidFencePlacing(col, row, Fence.DIRECTION.VERTICAL)):
                    validPlacings.append(FencePlacing(col, row, Fence.DIRECTION.VERTICAL))
        return validPlacings

    # TODO: check if it is blocking a player pawn
    def isValidFencePlacing(self, col, row, direction):
        if row in range(1, self.rows) and col in range(self.cols - 1) and direction == Fence.DIRECTION.HORIZONTAL and not self.hasFenceAtTop(col, row)  and not self.hasFenceAtTop(col + 1, row):
            for fence in self.fences:
                if (fence.col == col + 1 and fence.row == row - 1 and fence.direction == Fence.DIRECTION.VERTICAL):
                    return False
            return True
        if col in range(1, self.cols) and row in range(self.rows - 1) and direction == Fence.DIRECTION.VERTICAL   and not self.hasFenceAtLeft(col, row) and not self.hasFenceAtLeft(col, row + 1):
            for fence in self.fences:
                if (fence.col == col - 1 and fence.row == row + 1 and fence.direction == Fence.DIRECTION.HORIZONTAL):
                    return False
            return True
        return False

    def displayValidFencePlacings(self, player, validPlacings = None):
        if validPlacings is None:
            validPlacings = self.validFencePlacings()
        for validPlacing in validPlacings:
            possibleFence = Fence(self, player)
            possibleFence.col, possibleFence.row, possibleFence.direction = validPlacing.col, validPlacing.row, validPlacing.direction
            possibleFence.draw(Color.Lighter(player.color.value))
            del possibleFence

    def hideValidFencePlacings(self, player, validPlacings = None):
        if validPlacings is None: 
            validPlacings = self.validFencePlacings()
        for validPlacing in validPlacings:
            possibleFence = Fence(self, player)
            possibleFence.col, possibleFence.row, possibleFence.direction = validPlacing.col, validPlacing.row, validPlacing.direction
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
        if square is None or not self.isValidPawnMove(pawn, square.col, square.row):
            return None
        return PawnMove(pawn, square.col, square.row)

    def getFencePlacingFromMousePosition(self, x, y) -> FencePlacing:
        fullSize = self.squareSize + self.innerSize
        # on square space
        if self.getSquareFromMousePosition(x, y) is not None:
            return None
        # vertical fence
        if x % fullSize > self.squareSize and y % fullSize < self.squareSize:
            square = self.getSquareFromMousePosition(x + self.squareSize, y)
            return FencePlacing(square.col, square.row, Fence.DIRECTION.VERTICAL) if self.isValidFencePlacing(square.col, square.row, Fence.DIRECTION.VERTICAL) else None
        # horizontal fence
        if x % fullSize < self.squareSize and y % fullSize > self.squareSize:
            square = self.getSquareFromMousePosition(x, y + self.squareSize)
            return FencePlacing(square.col, square.row, Fence.DIRECTION.HORIZONTAL) if self.isValidFencePlacing(square.col, square.row, Fence.DIRECTION.HORIZONTAL) else None
        # on inner crossing space
        if x % fullSize > self.squareSize and y % fullSize > self.squareSize:
            square = self.getSquareFromMousePosition(x + self.squareSize, y + self.squareSize)
            direction = Fence.DIRECTION.HORIZONTAL if square.left - x < square.top - y else Fence.DIRECTION.VERTICAL
            return FencePlacing(square.col, square.row, direction) if self.isValidFencePlacing(square.col, square.row, direction) else None
        return None