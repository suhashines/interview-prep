def merge_interval(intervals):

    n = len(intervals)
    if n == 0:
        return []
    intervals.sort(key = lambda x: x[0])

    answer = [intervals[0]]

    for i in range(1,n):

        if intervals[i][0] > answer[-1][1]:
            # no overlapping
            answer.append(intervals[i])    
        else:
            # overlapping
            answer[-1][0] = min(answer[-1][0],intervals[i][0])
            answer[-1][1] = max(answer[-1][1],intervals[i][1])
    
    return answer

intervals =[[4,7],[1,4]]
print(merge_interval(intervals))