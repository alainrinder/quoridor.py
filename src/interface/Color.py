#
# Player.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#

from enum import Enum



class Color(Enum):
    RED       = "#c0392b"
    BLUE      = "#2980b9"
    GREEN     = "#27ae60"
    ORANGE    = "#f39c12"
    PURPLE    = "#8e44ad"
    TURQUOISE = "#16a085"
    WHITE     = "#ffffff"
    BLACK     = "#000000"
    SQUARE    = "#eeeeee"

    def FromRGB(r, g, b):
        return "#%02x%02x%02x" % (r, g, b)

    def Mix(color1, color2, ratio = 0.5):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        r, g, b = int(ratio*r1 + (1 - ratio)*r2), int(ratio*g1 + (1 - ratio)*g2), int(ratio*b1 + (1 - ratio)*b2)
        return Color.FromRGB(r, g, b)

    def Lighter(color, whiteRatio = 0.5):
        return Color.Mix(Color.WHITE.value, color, whiteRatio)

    def Darker(color, blackRatio = 0.5):
        return Color.Mix(Color.BLACK.value, color, blackRatio)

