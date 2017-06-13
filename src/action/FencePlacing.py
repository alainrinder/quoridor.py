#
# FencePlacing.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.action.IAction  import *
from src.interface.Fence import *



class FencePlacing(IAction):
    def __init__(self, coord, direction):
        self.coord     = coord
        self.direction = direction

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            #return self.__dict__ == other.__dict__
            return self.coord == other.coord and self.direction == other.direction
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
        return hash((self.coord, self.direction))

    def __str__(self):
        vertical = (self.direction == Fence.DIRECTION.VERTICAL)
        return "%s-fence at %s" % ("V" if vertical else "H", self.coord)


