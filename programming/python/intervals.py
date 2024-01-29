#!/usr/bin/env pytest

# https://github.com/hydrargyrum/junkyard
# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


import bisect
import math
from collections.abc import Collection


class Intervals(Collection):
    # list of intervals, e.g. [(1, 2), (4, 5)] for 1-2 and 4-5
    # no intervals overlap, if an interval is added that overlaps,
    # the union of overlapping intervals is stored, losing record of
    # previous intervals.
    # invariant: the list is always sorted

    def __init__(self, values=()):
        self.data = list(values)

    def _try_merge_after(self, point):
        while point + 1 < len(self.data) and self.data[point][1] >= self.data[point + 1][0]:
            self.data[point] = self.data[point][0], max(self.data[point][1], self.data[point + 1][1])
            del self.data[point + 1]

    def add_interval(self, a, b):
        assert a <= b
        point = bisect.bisect_left(self.data, (a, b))

        if point > 0:
            c, d = self.data[point - 1]
            assert c <= d
            assert c <= a
            # invariant: c, d < a, b
            # : c < a or (c == a and d < b)
            if a <= d:
                self.data[point - 1] = c, max(b, d)
                self._try_merge_after(point - 1)
                return

        if point < len(self.data):
            c, d = self.data[point]
            assert c <= d
            assert a <= c
            # invariant: a, b <= c, d
            # : a < c or (a == c and b <= d)
            if b > d:
                self.data[point] = min(a, c), max(b, d)
                self._try_merge_after(point)
                return
            elif b > c:
                self.data[point] = min(a, c), d
                return

        self.data.insert(point, (a, b))

    def get_interval_containing(self, value):
        point = bisect.bisect_right(self.data, (value, math.inf))
        # invariant: data[point][0] > value (because data[point][1] cannot be >= inf)
        if 0 < point:
            a, b = tup = self.data[point - 1]
            assert a <= value
            if value <= b:
                return tup

    def __getitem__(self, idx):
        return self.data[idx]

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, value):
        try:
            a, b = value
        except TypeError:
            return self.get_interval_containing(value) is not None
        # FIXME
        return self.get_interval_containing(a) is self.get_interval_containing(b)

    def __len__(self):
        return len(self.data)

    def __or__(self, other):
        ret = Intervals(self.data)
        for rng in other:
            ret.add_interval(*rng)
        return ret


def test_1():
    i = Intervals()

    # first interval
    i.add_interval(1, 2)
    assert list(i) == [(1, 2)]

    # duplicate
    i.add_interval(1, 2)
    assert list(i) == [(1, 2)]

    # append an interval
    i.add_interval(3, 4)
    assert list(i) == [(1, 2), (3, 4)]

    # prepend an interval
    i.add_interval(0, 0.5)
    assert list(i) == [(0, 0.5), (1, 2), (3, 4)]

    # overlap interval on right
    i.add_interval(0.25, 0.75)
    assert list(i) == [(0, 0.75), (1, 2), (3, 4)]

    # overlap absorbed
    i.add_interval(1.25, 1.75)
    assert list(i) == [(0, 0.75), (1, 2), (3, 4)]

    # overlap interval on left
    i.add_interval(1.25, 2.75)
    assert list(i) == [(0, 0.75), (1, 2.75), (3, 4)]

    # append an interval
    i.add_interval(5, 6)
    assert list(i) == [(0, 0.75), (1, 2.75), (3, 4), (5, 6)]

    # overlap 2 intervals: merge
    i.add_interval(2, 3)
    assert list(i) == [(0, 0.75), (1, 4), (5, 6)]

    # absorb all intervals
    i.add_interval(-1, 7)
    assert list(i) == [(-1, 7)]


def test_oper():
    i = Intervals()

    i.add_interval(1, 2)
    assert list(i) == [(1, 2)]

    assert 1 in i
    assert 1.5 in i
    assert 2 in i

    assert 3 not in i

    assert (1, 2) in i

    assert len(i) == 1
    assert i[0] == (1, 2)
