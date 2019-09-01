#
# GridCoordinates.py
#
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

import math

from src.Settings        import *
from src.action.PawnMove import *



class Path:
    """
    Find path for pawn
    """

    def __init__(self, moves):
        self.moves = moves

    def length(self):
        """
        Number of moves needed to access path target
        """
        return len(self.moves)

    def startCoord(self):
        """
        Coordinates where the path starts from
        """
        return self.moves[0].fromCoord

    def endCoord(self):
        """
        Coordinates where the path ends
        """
        return self.moves[-1].toCoord

    def firstMove(self):
        """
        First move of the path, which is the next move for pawn
        """
        return self.moves[0]

    def __str__(self):
        return "[%s] -> %s" % (str(self.startCoord()), " -> ".join(map(lambda move:str(move.toCoord), self.moves)))

    def ManhattanDistance(fromCoord, toCoord):
        """
        Manhattan distance (l1 norm) between 2 coordinates (4-connectivity)
        """
        return abs(toCoord.col - fromCoord.col) + abs(toCoord.row - fromCoord.row)

    def ManhattanDistanceMulti(fromCoord, toCoords):
        """
        Minimal manhattan distance between one coordinate and a set of target coordinates
        """
        minManhattanDistance = math.inf # 3.5
        for toCoord in toCoords:
            manhattanDistance = Path.ManhattanDistance(fromCoord, toCoord)
            if manhattanDistance < minManhattanDistance:
                minManhattanDistance = manhattanDistance
        return minManhattanDistance

    def BreadthFirstSearch(board, startCoord, endCoords, ignorePawns = False):
        """
        Path finding using breadth first search algorithm, from one coordinate to multiple targets.
        Set ignorePawns to True to find path as if there were no pawns at all (used to check if placing a fence will block a player)

        Algorithm:

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
                    Q.enqueue(n)
        """
        global TRACE
        TRACE["Path.BreadthFirstSearch"] += 1
        root = PawnMove(None, startCoord)

        previousMoves = {startCoord: root}
        nextMoves = [root]
        validPawnMoves = board.storedValidPawnMovesIgnoringPawns if ignorePawns else board.storedValidPawnMoves
        # While nodes remain to be visited
        while nextMoves:
            move = nextMoves.pop(0)
            for endCoord in endCoords:
                # If one of the targets is reached (shortest path)
                if move.toCoord == endCoord:
                    # Build backward path, then reverse it
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            # Add neighbors as nodes to visit
            validMoves = validPawnMoves[move.toCoord]
            # Sort neighbors to promote neighbors near targets
            sorted(validMoves, key=lambda validMove: Path.ManhattanDistanceMulti(validMove.toCoord, endCoords))
            for validMove in validMoves:
                if validMove.toCoord not in previousMoves:
                    previousMoves[validMove.toCoord] = validMove
                    nextMoves.append(validMove)
        return None

    def DepthFirstSearch():
        """
        Path finding using depth first search algorithm
        """
        pass

    def Dijkstra(board, startCoord, endCoords, moveScore = lambda move, step: 1, ignorePawns = False):
        """
        Path finding using Dijkstra algorithm.
        moveScore is a function used to define move distance: for instance, promoting path starting with a jump
        or discriminating path starting by offering a jump ti another player
        Set ignorePawns to True to find path as if there were no pawns at all (used to check if placing a fence will block a player)
        """
        global TRACE
        TRACE["Path.Dijkstra"] += 1
        root = PawnMove(None, startCoord)

        previousMoves = {startCoord: (0, root)} # coord: (score, move)
        nextMoves = [(0, 0, root)] # (step, score, move)
        validPawnMoves = board.storedValidPawnMovesIgnoringPawns if ignorePawns else board.storedValidPawnMoves
        # While nodes remain to be visited
        while nextMoves:
            sorted(nextMoves, key=lambda nextMove: nextMove[1]) # Order by score
            (step, score, move) = nextMoves.pop(0) # Get first (minimal score)
            for endCoord in endCoords:
                # If one of the targets is reached (shortest path)
                if move.toCoord == endCoord:
                    # Build backward path, then reverse it
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord][1]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            # Add neighbors as nodes to visit
            validMoves = validPawnMoves[move.toCoord]
            # Sort neighbors to promote neighbors near targets
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
        """
        Path finding using A* algorithm
        """
        pass
