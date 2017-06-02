#
# FencePlacing.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from src.action.IAction import *



class FencePlacing(IAction):
    def __init__(self, col, row, direction):
        self.col       = col
        self.row       = row
        self.direction = direction


