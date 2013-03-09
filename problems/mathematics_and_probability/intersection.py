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

import functools as ft
import itertools as it
import operator as op

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
        """the actual line is in t in [0,1] else outside i.e the infinite extension of the line"""
        return self.pa + self.delta*t
    def __str__(self):
        return "[{pa}, {pb}]".format(pa=self.pa, pb=self.pb)
    def __contains__(self, t):
        return 0<=t and t<=1 #closed set, T is considered as an intersection
    __repr__ = __str__

def intersect(line1, line2):
    det = (line1.delta.x*line2.delta.y - line2.delta.x*line1.delta.y)
    if(det):
        dp0 = line1.pa - line2.pa #delta p0
        s, t = (
            float(-line2.delta.y*dp0.x + line2.delta.x*dp0.y)/det,
            float(-line1.delta.y*dp0.x + line1.delta.x*dp0.y)/det,
        )
        print("{0}=={1}".format(line1(s), line2(t))) #consistent collision
        return (s in line1) and (t in line2)
    else:
        def inline(line1, line2):
            """check if two vectors conincide to see if they are inline"""
            v1 = line1.pa - line1.pb #two vectors with line1.pa as reference
            v2 = line1.pa - line2.pb #
            det = v1.x*v2.y-v1.y*v2.x
            return det==0.0 #little risky comparison but python mostly handles it well, they are actually only in line if this is true. but it might be possible to construction parallel inlines for which this returns false by roundoff errors.
    
        def overlapping(line1, line2):
            """ should handle verticle lines, some are tricky"""
            def inside(p, l, component):
                ps = map(component, [l.pa, l.pb])
                return min(*ps) <= component(p) and component(p) <= max(*ps)
            insidex = ft.partial(inside, component=op.attrgetter('x'))
            insidey = ft.partial(inside, component=op.attrgetter('y'))

            xwise, ywise = (
                sum(
                    it.starmap(
                        insidex,
                        it.chain(
                            it.product(
                                [line1.pa, line1.pb],
                                [line2,]
                            ),
                            it.product(
                                [line2.pa, line2.pb],
                                [line1,]
                            )
                        )
                    )
                ),
                sum(
                    it.starmap(
                        insidey,
                        it.chain(
                            it.product(
                                [line1.pa, line1.pb],
                                [line2,]
                            ),
                            it.product(
                                [line2.pa, line2.pb],
                                [line1,]
                            )
                        )
                    )
                )
            )
            assert(xwise==2 or xwise==0)
            assert(ywise==2 or ywise==0)
            return xwise==2 and ywise==2

        return inline(line1, line2) and overlapping(line1, line2)

print(intersect(
    line(point(  0,  0), point(  1,  1)), 
    line(point(  0,  1), point(  1,  0))
)) #intersect in (0.5,0.5)
print(intersect(
    line(point(0.5,  0), point(0.5,  1)), 
    line(point(  0,0.5), point(  1,0.5))
)) #intersect in (0.5,0.5)
print(not intersect(
    line(point(  0,  0), point(  0,  1)), 
    line(point(  1,  0), point(  1,  1))
)) #no intersection since parallel, and not in line
print(intersect(
    line(point(  0,  0), point(  1,  1)), 
    line(point(0.5,0.5), point(  2,  2))
)) #intersection since parallel and has common points 
print(intersect(
    line(point(  0,  0), point(  0,  1)), 
    line(point(  0,0.5), point(  1,0.5))
)) #T intersection
print(not intersect(
    line(point(0.5,  0), point(0.5,  1)), 
    line(point( 10,0.5), point( 11,0.5))
)) #no intersection

#whould need more tests, aspecially all specialcases, and perhaps doesn't handle lines with length of zero
