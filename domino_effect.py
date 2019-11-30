import sys
import heapq
from operator import itemgetter


lines = sys.stdin.readlines()
lines = list(map(lambda x: x.split(), lines))
lines = list(map(lambda x: tuple(list(map(int, x))), lines))
systems = []
i = 0
while lines[i] != (0, 0):
    n = lines[i][0]
    m = lines[i][1]
    adj_matrix = [[0] * n for j in range(n)]
    for row in lines[i + 1:i + 1 + m]:
        adj_matrix[row[0] - 1][row[1] - 1] = row[2]
        adj_matrix[row[1] - 1][row[0] - 1] = row[2]
    systems.append(adj_matrix)
    i += m + 1


def dijkstra(graph):
    min_heap = [0]
    dist = [-1] * len(graph[0])
    prev = [-1] * len(graph[0])
    dist[0] = 0
    while min_heap:
        u = heapq.heappop(min_heap)
        for v in range(len(graph[u])):
            if graph[u][v] > 0:
                alt = dist[u] + graph[u][v]
                if alt < dist[v] or dist[v] == -1:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(min_heap, v)
    return list(zip(dist, prev))


for i in range(len(systems)):
    adj_matrix = systems[i]
    # number of key dominoes
    n = len(adj_matrix[0])
    # list of distances to every node from node 0 with predecessors
    dist_prev = dijkstra(adj_matrix)
    max_time = max(dist_prev, key=itemgetter(0))
    max_node = dist_prev.index(max_time)
    # check if any edge unrelated to dijkstra could surpass the max_time
    max_after_node = -1
    node_pair = ()
    for v in range(n):
        for e in range(n):
            if adj_matrix[v][e] > 0:
                if e != dist_prev[v][1] and v != dist_prev[e][1]:
                    diff = abs(dist_prev[v][0] - dist_prev[e][0])
                    after_v = dist_prev[v][0] + (adj_matrix[v][e] - diff) / 2
                    if after_v > max_time[0] and after_v > max_after_node:
                        max_after_node = after_v
                        node_pair = (v, e) if v < e else (e, v)

    print('System #' + str(i + 1))
    if max_after_node != -1:
        print('The last domino falls after {} seconds, between key dominoes {} and {}.'.format(float(max_after_node),
                                                                                               node_pair[0] + 1,
                                                                                               node_pair[1] + 1))
    else:
        print('The last domino falls after {} seconds, at key domino {}.'.format(float(max_time[0]), max_node + 1))
    print('')