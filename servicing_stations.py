import sys

lines = sys.stdin.readlines()
lines = list(map(lambda x: x.split(), lines))
lines = list(map(lambda x: tuple(list(map(int, x))), lines))


def dfs(current, already_reachable, station_sum):
    global minimum
    # worst case
    if station_sum >= minimum:
        return
    # good case
    if already_reachable == n:
        minimum = station_sum

    for i in range(current):
        if not visited[i] and max_town_number[i] < current:
            return

    # call dfs with the next town
    dfs(current + 1, already_reachable, station_sum)
    # add towns
    a = 0
    tmp = [0] * n
    for i in range(n):
        if connected[current][i] and not visited[i]:
            visited[i] = 1
            tmp[a] = i
            a += 1
    if a == 0:
        return
    # check deeper
    dfs(current + 1, already_reachable + a, station_sum + 1)
    # reset visited
    for i in range(a):
        visited[tmp[i]] = 0


c = 0
while lines[c] != (0, 0):
    if lines[c] == (1, 0):
        print('1')
        c += 1
        continue
    n, m = lines[c]
    connected = [[0] * n for j in range(n)]
    for i in range(n):
        connected[i][i] = 1
    max_town_number = [0] * n
    visited = [0] * n
    minimum = n
    # fill adjacency matrix
    for row in lines[c + 1:c + 1 + m]:
        connected[row[0]-1][row[1]-1] = 1
        connected[row[1]-1][row[0]-1] = 1
    # fill max_town_number
    for i in range(n):
        for j in range(n):
            if connected[i][j] and max_town_number[i] < j+1:
                max_town_number[i] = j+1
    dfs(1, 0, 0)
    print(minimum)
    # read next input
    c += m + 1
