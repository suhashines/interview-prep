def insert_intervals(intervals,new_interval):

        n = len(intervals)
        answer = []

        # phase 1: add non overlapping intervals
        # end < new_interval.start
        i = 0

        while i<n and intervals[i][1] < new_interval[0] :
            answer.append(intervals[i])
            i += 1
        
        # phase 2: add overlapping intervals
        while i<n and intervals[i][0] <= new_interval[1] :

            new_interval[0] = min(intervals[i][0],new_interval[0])
            new_interval[1] = max(intervals[i][1],new_interval[1])
            i += 1
        answer.append(new_interval)

        # add the remaining

        while i<n :
            answer.append(intervals[i])
            i += 1
        return answer

intervals = [[2,3],[5,7]]
new_interval = [0,6]

print(insert_intervals(intervals,new_interval))

