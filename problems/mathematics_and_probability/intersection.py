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
#  line1(t) = line2(s)
#  delta1*t - delta2*s = p02 - p01
#
#  |delta1      0|(t)   
#  |     0 delta2|(s) = (p02 - p01)
#

