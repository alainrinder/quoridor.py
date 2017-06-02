#
# Game.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

import random

from src.Settings            import *
from src.interface.Board     import *
from src.interface.Pawn      import *
from src.player.Human        import *
from src.action.PawnMove     import *
from src.action.FencePlacing import *



class Game:
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
            players[i].pawn = Pawn(board, players[i])
            players[i].startPosition = board.startPosition(i)
            players[i].endPositions = board.endPositions(i)
            self.players.append(players[i])
            #board.addPawn(pawns[i])
        self.board = board

    def start(self, roundCount = 1):
        roundNumberZeroFill = len(str(roundCount))
        for roundNumber in range(1, roundCount + 1):
            print("ROUND #%s: " % str(roundNumber).zfill(roundNumberZeroFill), end="")
            playerCount = len(self.players)
            playerFenceCount = int(self.totalFenceCount/playerCount)
            self.board.fences, self.board.pawns = [], []
            for i in range(playerCount):
                player = self.players[i]
                player.pawn.place(player.startPosition.col, player.startPosition.row)
                for j in range(playerFenceCount):
                    player.fences.append(Fence(self.board, player))
            self.board.draw()
            
            currentPlayerIndex = random.randrange(playerCount) # COIN TOSS
            quitted, won = False, False
            while not quitted and not won:
                player = self.players[currentPlayerIndex]
                action = player.play(self.board)
                if isinstance(action, PawnMove):
                    player.movePawn(action.col, action.row)
                    for endPosition in player.endPositions:
                        if player.pawn.col == endPosition.col and player.pawn.row == endPosition.row:
                            won = True
                            print("Player %s won" % player.name)
                            player.score += 1
                elif isinstance(action, FencePlacing):
                    player.placeFence(action.col, action.row, action.direction)
                elif isinstance(action, Quit):
                    quitted = True
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