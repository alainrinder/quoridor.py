#
# PawnMove.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.action.IAction import *



class PawnMove(IAction):
    def __init__(self, fromCoord, toCoord, throughCoord = None):
        self.fromCoord    = fromCoord
        self.toCoord      = toCoord
        self.throughCoord = throughCoord

    def __str__(self):
    	return "from %s to %s%s" % (self.fromCoord, self.toCoord, " through %s" % self.throughCoord if self.throughCoord is not None else "") 

