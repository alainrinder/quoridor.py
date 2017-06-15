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

    def isJump(self):
    	return (self.throughCoord is not None)

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            #return self.__dict__ == other.__dict__
            return self.fromCoord == other.fromCoord and self.toCoord == other.toCoord and self.throughCoord == other.throughCoord
        return NotImplemented

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        #return hash(tuple(sorted(self.__dict__.items())))
        return hash((self.fromCoord, self.toCoord, self.throughCoord))

    def __str__(self):
    	return "from %s to %s%s" % (self.fromCoord, self.toCoord, " through %s" % self.throughCoord if self.throughCoord is not None else "") 

