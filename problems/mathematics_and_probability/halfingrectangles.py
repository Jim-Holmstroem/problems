#
# make one cut that halfs two rectangles
#
# cut through CM => rectangle is halfed
# thus if you make a line through both CM's you have it satisfied
#

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return point(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return point(self.x-other.x, self.y-other.y)
    def __mul__(self, c):
        return point(c*self.x, c*self.y)
    __rmul__ = __mul__
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    __repr__ = __str__

class line(object):
    """ infinite line defined by two points """
    def __init__(self, pa, pb):
        self.pa = pa
        self.pb = pb
    def __str__(self):
        return "[{},{}]".format(self.pa, self.pb)
    __repr__ = __str__

class rectangle(object):
    def __init__(self, pa, pb):
        """ pa and pb are two opposite corners"""
        self.pa = pa
        self.pb = pb
        self.cm = 0.5*(pb-pa)+pa
    def __str__(self):
        return "<{},{}>".format(self.pa, self.pb)
    __repr__ = __str__

def cutter(rect1, rect2):
    assert(isinstance(rect1, rectangle))
    assert(isinstance(rect2, rectangle))
    return line(rect1.cm, rect2.cm)

