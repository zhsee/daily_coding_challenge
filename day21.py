# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
import heapq


def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    heap = []
    for interval in intervals:
        if heap and interval[0] >= heap[0]:
            # room is already used in last meeting and continue to use the same room for this meeting
            heapq.heapreplace(heap, interval[1])

        else:
            heapq.heappush(heap, interval[1])

    return len(heap)


# assert find_minimum_room([(30, 75), (0, 50), (60, 150)]) == 2
# assert find_minimum_room([(30, 75), (0, 50), (0, 75), (60, 150)]) == 3
# print(minMeetingRooms([(30, 75), (0, 50), (60, 150)]))
print(minMeetingRooms([(30, 75), (30, 75), (30, 80), (30, 80), (0, 50), (0, 75), (0, 40), (60, 150), (0, 120)]))

