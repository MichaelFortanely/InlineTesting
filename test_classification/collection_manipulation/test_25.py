# https://github.com/qiyuangong/leetcode/blob/master/python/056_Merge_Intervals.py
from inline import Here

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals
        # sort by start
        print(intervals)
        temp = intervals.sort(key=lambda x: x[0])
        Here().given(intervals, [[4, 7], [5, 9]]).check_eq(temp, [[4, 7], [5, 9]])

        print(intervals)
        pos = 0
        while pos < len(intervals) - 1:
            # check overlap
            if intervals[pos][1] >= intervals[pos + 1][0]:
                next = intervals.pop(pos + 1)
                # check next is overlap or totally covered by pos
                if next[1] > intervals[pos][1]:
                    intervals[pos][1] = next[1]
            # print [(t.start, t.end) for t in intervals], pos
            else:
                pos += 1
        return intervals


s = Solution()
print (s.merge([[5, 10],[1,3],[2,6],[8,10],[15,18]]))