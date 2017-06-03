#
# GridCoordinates.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#



class Path:
    def __init__(self, coords):
        self.coords = coords

    def length(self):
        return len(self.coords)

    def start(self):
        return self.coords[0]

    def end(self):
        return self.coords[-1]

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
        #alreadyVisited = [(startCoord, None)]
        #forthcomingVisited = [(startCoord, None)]
        #while forthcomingVisited:
        #    node = forthcomingVisited.pop(0) 
        #    for endCoord in endCoords:
        #        if node.coord == endCoord:
        #            return 
        #    for neighbor in node.coord.neighbors(board): # validpawnmoves


    def DepthFirstSearch():
        pass

    def Djikstra():
        pass

    def AStar():
        pass

