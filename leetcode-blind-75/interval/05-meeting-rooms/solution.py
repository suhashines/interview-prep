def meeting_rooms(intervals):
    n = len(intervals)
    intervals.sort(key = lambda x: x[0])
    for i in range(n-1):

        if intervals[i+1][0] < intervals[i][1] :
            # we have an overlap
            return False
    return True

intervals = [[4,10],[2,4]]
print(meeting_rooms(intervals))