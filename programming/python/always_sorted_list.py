
"""Always sorted list

Use add() instead of append() or insert().
"""

import bisect


class SortedList(list):
    def __init__(self, *iterable):
        super().__init__(*iterable)
        super().sort()

    def find_lt(self, v):
        return bisect.bisect_left(self, v)

    def find_rt(self, v):
        return bisect.bisect_right(self, v)

    def add(self, v):
        bisect.insort_left(self, v)

    def _find(self, v):
        pos = bisect.bisect_left(self, v)
        if pos < len(self) and self[pos] == v:
            return pos
        return -1

    # 'list' interface
    def __contains__(self, v):
        return self._find(v) >= 0

    def remove(self, v):
        pos = self._find(v)
        if pos < 0:
            raise ValueError('%r not in SortedList' % v)
        else:
            del self[pos]

    def extend(self, iterable):
        for v in iterable:
            self.add(v)

    def append(self, v):
        raise TypeError('cannot append values in SortedList')

    def index(self, v):
        pos = self._find(v)
        if pos < 0:
            raise ValueError('%r not in SortedList' % v)
        return pos

    def count(self, v):
        pos = self.find_lt(v)
        count = 0
        for pos in range(pos, len(self)):
            if self[pos] != v:
                break
            count += 1
        return count


def assert_raises(exc_type, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exc_type:
        pass
    else:
        assert False, '%r was not raised' % exc_type


def test_SortedList():
    li = SortedList([4, 3, 1, 2])
    assert li == [1, 2, 3, 4]

    li.add(0.5)
    assert li == [0.5, 1, 2, 3, 4]

    li.add(4.5)
    assert li == [0.5, 1, 2, 3, 4, 4.5]

    li.add(1.5)
    assert li == [0.5, 1, 1.5, 2, 3, 4, 4.5]

    assert li[li.find_lt(0.5)] == 0.5
    assert li[li.find_lt(3)] == 3
    assert li[li.find_lt(4.5)] == 4.5

    assert li[li.find_lt(0)] == 0.5
    assert li.find_lt(5) == len(li)

    assert li.index(1.5) == 2
    assert_raises(ValueError, li.index, 5)

    assert 2 in li
    li.remove(2)
    assert li == [0.5, 1, 1.5, 3, 4, 4.5]
    assert 2 not in li
    assert_raises(ValueError, li.remove, 2)
