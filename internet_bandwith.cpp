#include <algorithm>
#include <cstring>
#include <cstdio>
#include <limits>
#include <queue>
using namespace std;
 
#define N 100
// n is the number of vertices, s the source and t the sink
int adjacencyMatrix[N][N], parent[N], n, s, t;
 
bool bfs() {
    queue<int> q;
    q.push(s);
    memset(parent, -1, sizeof parent);
    parent[s] = s;
    while (q.size()) {
        int u = q.front();
        q.pop();
        if (u == t)
            return true;
        for (int v = 0; v < n; ++v)
            if (parent[v] == -1 && adjacencyMatrix[u][v])
                parent[v] = u, q.push(v);
    }
    return false;
}
 
int maxFlow() {
    int mf = 0, f, v;
    while (bfs()) {
        // find the minimum path
        v = t;
        f = numeric_limits<int>::max();
        while (parent[v] != v)
            f = min(f, adjacencyMatrix[parent[v]][v]), v = parent[v];
        // decrease all weights along the path
        v = t;
        mf += f;
        while (parent[v] != v)
            adjacencyMatrix[parent[v]][v] -= f, adjacencyMatrix[v][parent[v]] += f, v = parent[v];
    }
    return mf;
}
 
#define con(i, j, c) adjacencyMatrix[i][j] += c, adjacencyMatrix[j][i] += c
int main() {
    int c, scenario = 0;
    while (scanf("%d", &n) == 1 && n) {
        // process input
        memset(adjacencyMatrix, 0, sizeof adjacencyMatrix);
        scanf("%d %d %d", &s, &t, &c);
        --s, --t;
        for (int i = 0, x, y, z; i < c; ++i)
            scanf("%d %d %d", &x, &y, &z), con(x - 1, y - 1, z);
        printf("Network %d\n", ++scenario);
        printf("The bandwidth is %d.\n\n", maxFlow());
    }
    return 0;
}