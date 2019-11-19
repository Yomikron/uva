import sys


lines = sys.stdin.readlines()
i = 0
# list of adjacency matrices
adj_matrices = []
# list of list of location names in the same order they appear in the adj_matrix
list_of_locations = []
while True:
    total_locations = int(lines[i])
    if total_locations == 0:
        break
    i += 1
    locations = list(map(lambda x: x.strip(), lines[i:i+total_locations]))
    list_of_locations.append(locations)
    i += total_locations
    adj_matrix = [[0] * total_locations for j in range(total_locations)]
    total_routes = int(lines[i])
    i += 1
    routes = list(map(lambda x: x.split(), lines[i:i+total_routes]))
    i += total_routes
    for route in routes:
        route_start, route_end = locations.index(route[0]), locations.index(route[1])
        adj_matrix[route_start][route_end] = 1
        adj_matrix[route_end][route_start] = 1
    adj_matrices.append(adj_matrix)


def dfs(v, p=-1):
    global timer
    visited[v] = True
    timer += 1
    tin[v] = low[v] = timer
    children = 0
    # for each w adjacent to v
    for w in range(n):
        if matrix[v][w] != 0:
            if w == p:
                continue
            if visited[w]:
                low[v] = min(low[v], tin[w])
            else:
                dfs(w, v)
                low[v] = min(low[v], low[w])
                # none of w or its descendants has a back edge to any ancestor of v
                if low[w] >= tin[v] and p != -1:
                    articulation_points.add(v)
                children += 1
    # v is root
    if p == -1 and children > 1:
        articulation_points.add(v)


for m in range(len(adj_matrices)):
    matrix = adj_matrices[m]
    # n is the number of locations
    n = len(matrix[0])
    # set of found art_points
    articulation_points = set()
    # counts the steps until we visit any node
    timer = 0
    visited = [False] * n
    # time of entry into node
    tin = [-1] * n
    # minimum of tin[v], tin[p], low[w]
    low = [-1] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
    ap = len(articulation_points)
    print('City map #' + str(m+1) + ': ' + str(ap) + ' camera(s) found')
    articulation_points = list(map(lambda x: list_of_locations[m][x], articulation_points))
    articulation_points.sort()
    for a in articulation_points:
        print(a)
    if m < len(adj_matrices)-1:
        print('')