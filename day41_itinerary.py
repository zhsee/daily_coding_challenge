# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.


# no working for flight with cycle loop
def itinerary(start):
    print(route)
    if len(route) == N_route:
        route.append(start)
        return True
    if start in flights:
        route.append(start)
        if itinerary(flights[start]):
            return True
        route.pop()
    return False



# alist = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# start = 'YUL'
alist = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
# alist = [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')]
start = 'A'

flights = dict(alist)
N_route = len(flights)
route = []

if itinerary(start):
    print(route)
else:
    print('no route')


# def get_itinerary(flights, current_itinerary):
#     # If we've used up all the flights, we're done
#     if not flights:
#         return current_itinerary
#     last_stop = current_itinerary[-1]
#     for i, (origin, destination) in enumerate(flights):
#         # Make a copy of flights without the current one to mark it as used
#         flights_minus_current = flights[:i] + flights[i + 1:]
#         current_itinerary.append(destination)
#         if origin == last_stop:
#             return get_itinerary(flights_minus_current, current_itinerary)
#         current_itinerary.pop()
#     return None

# print(get_itinerary(alist, ['A']))
