

#                 7 - 6
#               /
# 2 - 1 - 0 - 3   | / |
#               \
#                 4 - 5

# find shortest path from 0 to 7 and from 2 to 6

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def search(self, s, e):
        found = False
        queue = []
        visited = set()
        via = {}

        queue.append(s)
        via[s] = ""

        while queue and not found:
            n = queue.pop(0)
            if n == e:
                found = True
            else:
                for a in self.graph[n]:
                    if not (a in queue or a in visited):
                        queue.append(a)
                        via[a] = n
            visited.add(n)


        if found:
            result = self.get_trace(via, s, e)
            print(f'shortest distance from {s} to {e}: {len(result) - 1}')
            print(f'path: {", ".join(map(str, result))}')
            print()
        else:
            return None


    def get_trace(self, via_hash, start, end):
        trace = [end]
        while start not in trace:
            trace.append(via_hash[end])
            end = via_hash[end]
        return trace[::-1]


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(3, 7)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(4, 7)
g.addEdge(5, 6)
g.addEdge(6, 7)

g.search(0, 7)
g.search(2, 6)
g.search(3, 4)
