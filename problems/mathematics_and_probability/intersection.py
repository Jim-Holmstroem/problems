#
# intersect(line1, line2)
#
# Idea: intersection of infinite lines and that collision point is within both bounding boxes of the lines.
# 
# Intersection of infinite lines:
#   
#  line1(t) = delta1*t+p01
#  line2(s) = delta2*s+p02
#
#  line1(t_i) = line2(s_i)
#  delta1*t_i - delta2*s_i = p02 - p01
#
#  [[delta1 -delta2] (t_i)   
#   [  |       |   ]](s_i) = (p02 - p01)
#
#  (t_i)   [[delta1 -delta2]^-1 
#  (s_i) =  [  |       |   ]]  (p02-p01)
#
#  [[a b]^-1           [[ d -b]
#   [c d]]  = (ad-bc)^-1[-c  a]]
#  
#  and for our case
#                                          [[-delta2.y  delta2.x]  (deltap0.x)
#  (delta1.x*delta2.y-delta2.x*delta1.y)^-1 [-delta1.y  delta1.x]] (deltap0.y) =
#  = (det)^-1(
#     -delta2.y*deltap0.x+delta2.x*deltap0.y, 
#     -delta1.y*deltap0.x+delta1.x*deltap0.y
#  )
#
#  then we just need to check the bounding boxes
#  line1(t_i) in boundingbox(line1) and line2(s_i) in boundingbox(line2) 
#  that is, is the intersection with each lines boundingbox given their own parameter?
#

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return point(self.x+other.x, self.y+other.y)
    def __neg__(self):
        return point(-self.x, -self.y)
    def __sub__(self, other):
        return self+(-other)
    def __mul__(self, other):
        return point(other*self.x, other*self.y)
    __rmul__ = __mul__
    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)
    __repr__ = __str__ 

class line(object):
    """ starts at pa and goes to pb"""
    def __init__(self, pa, pb):
        self.pa = pa
        self.pb = pb
        self.delta = pb-pa
    def __call__(self, t):
        return self.pa + self.delta*t
    def __str__(self):
        return "[{pa}, {pb}]".format(pa=self.pa, pb=self.pb)
    __repr__ = __str__

def intersect(line1, line2):
    det = (line1.delta.x*line2.delta.y - line2.delta.x*line1.delta.y)
    dp0 = line1.pa - line2.pa #delta p0
    s, t = (
        float(-line2.delta.y*dp0.x + line2.delta.x*dp0.y)/det,
        float(-line1.delta.y*dp0.x + line1.delta.x*dp0.y)/det,
    )
    print(line1(s))
    print(line2(t))

intersect(line(point(0,0),point(1,1)),line(point(0,1),point(1,0))) #intersect in (0.5,0.5)
