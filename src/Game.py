#
# Game.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

import random

from src.Settings            import *
from src.interface.Color     import *
from src.interface.Board     import *
from src.interface.Pawn      import *
from src.player.Human        import *
from src.action.PawnMove     import *
from src.action.FencePlacing import *
from src.Path                import *



class Game:
    def DefaultColorForPlayer(i):
        switcher = {
            0: Color.RED,
            1: Color.BLUE,
            2: Color.GREEN,
            3: Color.ORANGE
        }
        return switcher[i]

    def DefaultNameForPlayer(i):
        switcher = {
            0: "A",
            1: "B",
            2: "C",
            4: "D"
        }
        return switcher[i]

    def __init__(self, players, cols = 9, rows = 9, totalFenceCount = 20, squareSize = 32, innerSize = None):
        if innerSize is None:
            innerSize = int(squareSize/8)
        self.totalFenceCount = totalFenceCount
        board = Board(self, cols, rows, squareSize, innerSize)
        playerCount = min(int(len(players)/2)*2, 4)
        self.players = []
        for i in range(playerCount):
            if INTERFACE and isinstance(players[i], Human):
                raise Exception("Cannot launch a blind game with human players")
            if players[i].name is None:
                players[i].name = Game.DefaultNameForPlayer(i)
            if players[i].color is None:
                players[i].color = Game.DefaultColorForPlayer(i)
            players[i].pawn = Pawn(board, players[i])
            players[i].startPosition = board.startPosition(i)
            players[i].endPositions = board.endPositions(i)
            self.players.append(players[i])
            #board.addPawn(pawns[i])
        self.board = board

    def start(self, roundCount = 1):
        roundNumberZeroFill = len(str(roundCount))
        for roundNumber in range(1, roundCount + 1):
            self.board.draw()
            print("ROUND #%s: " % str(roundNumber).zfill(roundNumberZeroFill), end="")
            playerCount = len(self.players)
            playerFenceCount = int(self.totalFenceCount/playerCount)
            self.board.fences, self.board.pawns = [], []
            for i in range(playerCount):
                player = self.players[i]
                player.pawn.place(player.startPosition)
                for j in range(playerFenceCount):
                    player.fences.append(Fence(self.board, player))
            
            currentPlayerIndex = random.randrange(playerCount) # COIN TOSS
            finished = False
            while not finished:
                player = self.players[currentPlayerIndex]
                action = player.play(self.board)
                path = Path.BreadthFirstSearch(self.board, player.pawn.coord, player.endPositions)
                #self.board.displayPath(path, player.color.value)
                #time.sleep(0.5)
                #self.board.hidePath(path)
                #print(path)
                if isinstance(action, PawnMove):
                    player.movePawn(action.toCoord)
                    if player.hasWon():
                        finished = True
                        print("Player %s won" % player.name)
                        player.score += 1
                elif isinstance(action, FencePlacing):
                    player.placeFence(action.coord, action.direction)
                elif isinstance(action, Quit):
                    finished = True
                    print("Player %s quitted" % player.name)
                currentPlayerIndex = (currentPlayerIndex + 1) % playerCount
                if INTERFACE:
                	time.sleep(TEMPO_SEC)
            # DELETE OBJECTS (fences in board.fences, ...)
        print()
        print("FINAL SCORES: ")
        bestPlayer = self.players[0]
        for player in self.players:
            print("- %s: %d" % (str(player), player.score))
            if player.score > bestPlayer.score: 
            	bestPlayer = player
        print("Player %s won with %d victories!" % (bestPlayer.name, bestPlayer.score))

    def end(self):
        if INTERFACE:
            self.board.window.close()

