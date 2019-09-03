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
    """
    Define players and game parameters, and manage game rounds.
    """

    DefaultColorForPlayer = [
        Color.RED,
        Color.BLUE,
        Color.GREEN,
        Color.ORANGE
    ]

    DefaultNameForPlayer = [
        "1",
        "2",
        "3",
        "4"
    ]

    def __init__(self, players, cols = 9, rows = 9, totalFenceCount = 20, squareSize = 32, innerSize = None):
        if innerSize is None:
            innerSize = int(squareSize/8)
        self.totalFenceCount = totalFenceCount
        # Create board instance
        board = Board(self, cols, rows, squareSize, innerSize)
        # Support only 2 or 4 players
        playerCount = min(int(len(players)/2)*2, 4)
        self.players = []
        # For each player
        for i in range(playerCount):
            if not INTERFACE and isinstance(players[i], Human):
                raise Exception("Cannot launch a blind game with human players")
            # Define player name and color
            if players[i].name is None:
                players[i].name = Game.DefaultNameForPlayer[i]
            if players[i].color is None:
                players[i].color = Game.DefaultColorForPlayer[i]
            # Initinialize player pawn
            players[i].pawn = Pawn(board, players[i])
            # Define player start positions and targets
            players[i].startPosition = board.startPosition(i)
            players[i].endPositions = board.endPositions(i)
            self.players.append(players[i])
        self.board = board

    def start(self, roundCount = 1):
        """
        Launch a series of rounds; for each round, ask successively each player to play.
        """
        roundNumberZeroFill = len(str(roundCount))
        # For each round
        for roundNumber in range(1, roundCount + 1):
            # Reset board stored valid pawn moves & fence placings, and redraw empty grid
            self.board.initStoredValidActions()
            self.board.draw()
            print("ROUND #%s: " % str(roundNumber).zfill(roundNumberZeroFill), end="")
            playerCount = len(self.players)
            # Share fences between players
            playerFenceCount = int(self.totalFenceCount/playerCount)
            self.board.fences, self.board.pawns = [], []
            # For each player
            for i in range(playerCount):
                player = self.players[i]
                # Place player pawn at start position and add fences to player stock
                player.pawn.place(player.startPosition)
                for j in range(playerFenceCount):
                    player.fences.append(Fence(self.board, player))
            # Define randomly first player (coin toss)
            currentPlayerIndex = random.randrange(playerCount)
            finished = False
            while not finished:
                player = self.players[currentPlayerIndex]
                # The player chooses its action (manually for human players or automatically for bots)
                action = player.play(self.board)
                if isinstance(action, PawnMove):
                    player.movePawn(action.toCoord)
                    # Check if the pawn has reach one of the player targets
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
        print()
        #self.board.drawOnConsole()
        # Display final scores
        print("FINAL SCORES: ")
        bestPlayer = self.players[0]
        for player in self.players:
            print("- %s: %d" % (str(player), player.score))
            if player.score > bestPlayer.score:
            	bestPlayer = player
        print("Player %s won with %d victories!" % (bestPlayer.name, bestPlayer.score))

    def end(self):
        """
        Called at the end in order to close the window.
        """
        if INTERFACE:
            self.board.window.close()
