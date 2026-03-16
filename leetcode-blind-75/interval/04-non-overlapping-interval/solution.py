def erase_overlap(intervals):

    n = len(intervals)

    if n == 0:
        return 0
    intervals.sort(key = lambda x: x[1])
    prev = 0
    cnt = 0

    for i in range(1,n):

        if intervals[i][0] >= intervals[prev][1]:
            # no overlapping
            prev = i
         
        else:
            # overlapping found
            cnt += 1
    return cnt

intervals = [[1,100],[11,22],[1,11],[2,12]]

print(erase_overlap(intervals))