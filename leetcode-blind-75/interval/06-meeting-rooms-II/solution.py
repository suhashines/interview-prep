def min_meeting_rooms(intervals):

    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    rooms,maxRooms = 0,0
    s,e = 0,0

    while s<len(start):

        # has a meeting started before the other one ended
        # that means we need to allocate a room
        if start[s] < end[e] :
            s += 1
            rooms += 1
        else:
            # that means a meeting has ended just now
            # so we can free a room
            rooms -= 1
            e += 1
        maxRooms = max(maxRooms,rooms)
    return maxRooms

intervals = [[7,10],[2,4]]
print(min_meeting_rooms(intervals))