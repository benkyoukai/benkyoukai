import sys
import os

sys.path.append(os.path.abspath("../merge_sort"))

from merge_sort import *

def min_distance_1d(points):
    if len(points) < 2: return None

    points = merge_sort(points)
    (pre, cur), points = points[:2], points[2:]
    min_ds = abs(cur - pre)

    for pt in points:
        ds = abs(pt - cur)
        if ds < min_ds: min_ds = ds
        cur = pt

    return min_ds

def min_distance_2d(points): pass

min_distance = min_distance_2d

if __name__ == "__main__":
    assert min_distance_1d([1]) is None
    assert min_distance_1d([1,3]) == 2
    assert min_distance_1d([1,3,6,10,11]) == 1
    print "=> passed"

