#
# IBot.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.player.IPlayer import *



class IBot(IPlayer):
    def __str__(self):
        return "[BOT] %s (%s)" % (self.name, self.color.name)