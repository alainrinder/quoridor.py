#
# GridCoordinates.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.action.PawnMove import *



class Path:
    def __init__(self, coords):
        self.coords = coords

    def length(self):
        return len(self.coords)

    def start(self):
        return self.coords[0]

    def end(self):
        return self.coords[-1]

    def __str__(self):
        return " -> ".join(map(str, self.coords))

    # l1 norm
    def ManhattanDistance(coord1, coord2):
        return abs(coord2.col - coord1.col) + abs(coord2.row - coord1.row);

    def BreadthFirstSearch(board, startCoord, endCoords):
        """Breadth-First-Search(Graph, root):
        
        create empty set S
        create empty queue Q      

        add root to S
        Q.enqueue(root)                      

        while Q is not empty:
            current = Q.dequeue()
            if current is the goal:
                return current
            for each node n that is adjacent to current:
                if n is not in S:
                    add n to S
                    n.parent = current
                    Q.enqueue(n)"""
        root = PawnMove(None, startCoord)

        previousMoves = {(startCoord.col, startCoord.row): root}
        nextMoves = [root]
        while nextMoves:
            move = nextMoves.pop(0) 
            for endCoord in endCoords:
                if move.toCoord == endCoord:
                    # Found shortest path
                    coords = [move.toCoord]
                    while move.fromCoord is not None:
                        move = previousMoves[(move.fromCoord.col, move.fromCoord.row)]
                        coords.append(move.toCoord)
                    coords.reverse()
                    return Path(coords)
            # Add neighbors
            for validMove in board.validPawnMoves(move.toCoord): 
                if (validMove.toCoord.col, validMove.toCoord.row) not in previousMoves:
                    previousMoves[(validMove.toCoord.col, validMove.toCoord.row)] = validMove
                    nextMoves.append(validMove)

    def DepthFirstSearch():
        pass

    def Djikstra():
        pass

    def AStar():
        pass

