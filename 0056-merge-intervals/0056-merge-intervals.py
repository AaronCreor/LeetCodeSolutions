class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        i=0
        x = len(intervals)-1
        while i < x:
            if ((intervals[i][0] <= intervals[i+1][0]) and intervals[i][1] >= intervals[i+1][0]):
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i)
                x=x-1
                continue
            else:
                i+=1
                continue
        return intervals

        #for i in range(x):
        #    if ((intervals[i][0] <= intervals[i+1][0]) and intervals[i][1] >= intervals[i+1][0]):
        #        intervals[i+1][0] = intervals[i][0]
        #        intervals.pop(i)
        #    else:
        #        continue
        #return intervals