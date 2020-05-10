"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/0000000000045875
Valid algorithm, but it's just too slow for the large test set :(
"""
from collections import deque


def bfs(capacities, source, sink):
    """
    Find path from source to sink with non-zero capacity, if it exists.
    """
    next_vertices = deque()
    visited = [False] * len(capacities)
    visited[source] = True
    parents = [-1] * len(capacities)
    next_vertices.append(source)
    while next_vertices:
        u = next_vertices.popleft()
        vs = capacities[u]
        for v, c in enumerate(vs):
            if not visited[v] and c > 0:
                next_vertices.append(v)
                visited[v] = True
                parents[v] = u
                if v == sink:
                    return parents
    return None


def ford_fulkerson(edges, vertices, source, sink):
    """
    Given a dict of edge capacities in the form `{(u,v): c}`, returns a V*V
    array `f` of the optimal flow from source to sink, where f[u][v] is the flow
    from vertex u to vertex v.
    """
    flow = []
    capacities = []
    max_capacity = 0
    for _ in range(vertices):
        flow.append([0] * vertices)
        capacities.append([0] * vertices)
    for (i, j), c in edges.items():
        capacities[i][j] = c
        max_capacity = max(max_capacity, c)

    while True:
        path = bfs(capacities, source, sink)
        if not path:
            return flow
        capacity = max_capacity
        v = sink
        u = path[v]
        while u != -1:
            capacity = min(capacity, capacities[u][v])
            v = u
            u = path[u]
        v = sink
        u = path[v]
        while u != -1:
            flow[u][v] += capacity
            flow[v][u] -= capacity
            capacities[u][v] -= capacity
            capacities[v][u] += capacity
            v = u
            u = path[u]


def solve_case(grid):
    n = len(grid)
    by_value = {}
    count_by_value = {}

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col not in by_value:
                by_value[col] = {}
                count_by_value[col] = 0
            by_value[col][(1 + i, n + 1 + j)] = 1
            by_value[col][(0, 1 + i)] = 1
            by_value[col][(n + 1 + j, 2 * n + 1)] = 1
            count_by_value[col] += 1

    for k, v in by_value.items():
        flow = ford_fulkerson(v, 2 * n + 2, 0, 2 * n + 1)
        max_flow = sum(flow[0][i] for i in range(1, n + 1))
        count_by_value[k] -= max_flow

    return sum(x for x in count_by_value.values())


def run():
    cases = int(input())
    for i in range(1, cases + 1):
        n = int(input())
        grid = []
        for _ in range(n):
            grid.append([int(x) for x in input().split(" ")])
        soln = solve_case(grid)
        print("Case #{}: {}".format(i, soln), flush=True)


if __name__ == "__main__":
    run()
