#
# GridCoordinates.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

import math

from src.action.PawnMove import *



class Path:
    def __init__(self, moves):
        self.moves = moves

    def length(self):
        return len(self.moves)

    def startCoord(self):
        return self.moves[0].fromCoord

    def endCoord(self):
        return self.moves[-1].toCoord

    def firstMove(self):
        return self.moves[0]

    def __str__(self):
        return "[%s] -> %s" % (str(self.startCoord()), " -> ".join(map(lambda move:str(move.toCoord), self.moves)))

    # l1 norm
    def ManhattanDistance(fromCoord, toCoord):
        return abs(toCoord.col - fromCoord.col) + abs(toCoord.row - fromCoord.row)

    def ManhattanDistanceMulti(fromCoord, toCoords):
        minManhattanDistance = math.inf # 3.5
        for toCoord in toCoords:
            manhattanDistance = Path.ManhattanDistance(fromCoord, toCoord)
            if manhattanDistance < minManhattanDistance:
                minManhattanDistance = manhattanDistance
        return minManhattanDistance

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

        previousMoves = {startCoord: root}
        nextMoves = [root]
        while nextMoves:
            move = nextMoves.pop(0) 
            for endCoord in endCoords:
                if move.toCoord == endCoord:
                    # Found shortest path
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            # Add neighbors
            validMoves = board.validPawnMoves(move.toCoord)
            sorted(validMoves, key=lambda validMove: Path.ManhattanDistanceMulti(validMove.toCoord, endCoords))
            for validMove in validMoves: 
                if validMove.toCoord not in previousMoves:
                    previousMoves[validMove.toCoord] = validMove
                    nextMoves.append(validMove)
        return None

    def DepthFirstSearch():
        pass

    def Dijkstra(board, startCoord, endCoords, moveScore = lambda move, step: 1): # moveScore = function or lamdba (move) promotePathStartingWithJump, discriminatePathStartigByOfferingJump
        root = PawnMove(None, startCoord)

        previousMoves = {startCoord: (0, root)} # coord: (score, move)
        nextMoves = [(0, 0, root)] # (step, score, move)
        while nextMoves:
            sorted(nextMoves, key=lambda nextMove: nextMove[1]) # Order by score
            (step, score, move) = nextMoves.pop(0) # Get first (minimal score)
            for endCoord in endCoords:
                if move.toCoord == endCoord: # Found shortest path
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord][1]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            # Add neighbors
            validMoves = board.validPawnMoves(move.toCoord)
            sorted(validMoves, key=lambda validMove: Path.ManhattanDistanceMulti(validMove.toCoord, endCoords))
            for validMove in validMoves: 
                validMoveScore = score + moveScore(validMove, step + 1)
                if validMove.toCoord not in previousMoves:
                    previousMoves[validMove.toCoord] = (validMoveScore, validMove)
                    nextMoves.append((step + 1, validMoveScore, validMove))
                if validMoveScore < previousMoves[validMove.toCoord][0]:
                    previousMoves[validMove.toCoord] = (validMoveScore, validMove)
        return None

    def AStar():
        pass

