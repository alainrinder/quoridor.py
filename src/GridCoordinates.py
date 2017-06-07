#
# GridCoordinates.py
# 
# @author    Alain Rinder
# @date      2017.06.02
# @version   0.1
#



class GridCoordinates:
    def __init__(self, col, row):
        self.col  = col
        self.row  = row

    def left(self):
    	return GridCoordinates(self.col - 1, self.row)

    def right(self):
    	return GridCoordinates(self.col + 1, self.row)

    def top(self):
    	return GridCoordinates(self.col, self.row - 1)

    def bottom(self):
    	return GridCoordinates(self.col, self.row + 1)

    def clone(self):
    	return GridCoordinates(self.col, self.row)

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            #return self.__dict__ == other.__dict__
            return self.col == other.col and self.row == other.row
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
        return hash((self.col, self.row))


    def __str__(self):
    	return "%d,%d" % (self.col, self.row)


