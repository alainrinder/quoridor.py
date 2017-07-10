#
# GridCoordinates.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#



class GridCoordinates:
    """
    Coordinates on square grid
    """

    def __init__(self, col, row):
        self.col  = col
        self.row  = row

    def left(self):
        """
        Return the coordinates of the square at left, even if it does not exists
        """
        return GridCoordinates(self.col - 1, self.row)

    def right(self):
        """
        Return the coordinates of the square at right, even if it does not exists
        """
        return GridCoordinates(self.col + 1, self.row)

    def top(self):
        """
        Return the coordinates of the square at top, even if it does not exists
        """
        return GridCoordinates(self.col, self.row - 1)

    def bottom(self):
        """
        Return the coordinates of the square at bottom, even if it does not exists
        """
        return GridCoordinates(self.col, self.row + 1)

    def clone(self):
        """
        Return identical coordinates 
        """
        return GridCoordinates(self.col, self.row)

    def __eq__(self, other):
        """
        Override the default Equals behavior.
        https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
        """
        if isinstance(other, self.__class__):
            #return self.__dict__ == other.__dict__
            return self.col == other.col and self.row == other.row
        return NotImplemented

    def __ne__(self, other):
        """
        Define a non-equality test.
        https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
        """
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """
        Override the default hash behavior (that returns the id or the object).
        https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
        """
        return hash((self.col, self.row))

    def __str__(self):
        return "%d,%d" % (self.col, self.row)


