# Time:  O(n)
# Space: O(k)
"""
Problem description
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
 

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your q structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

    def next(self):
        """
        :rtype: int
        """

    def hasNext(self):
        """
        :rtype: bool
        """

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())