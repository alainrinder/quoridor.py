#
# FencePlacing.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.action.IAction import *



class FencePlacing(IAction):
    def __init__(self, coord, direction):
        self.coord     = coord
        self.direction = direction


