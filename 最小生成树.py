import heapq


def prim(graph):
    num_vertices = len(graph)
    min_heap = [(0, 0)]  # 存储边的权重和目标节点
    visited = set()  # 存储已访问的节点
    min_spanning_tree = []  # 存储最小生成树的边

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)

        if vertex not in visited:
            visited.add(vertex)
            if weight > 0:
                min_spanning_tree.append((vertex, weight))

            for neighbor, edge_weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return min_spanning_tree


# 示例图的邻接列表表示（无向图）
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 4), (3, 5)],
    2: [(0, 3), (1, 4), (4, 6)],
    3: [(1, 5)],
    4: [(2, 6)]
}

min_spanning_tree = prim(graph)
print("最小生成树的边：", min_spanning_tree)


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


def kruskal(graph):
    edges = []  # 存储边的列表，格式为 (weight, u, v)
    num_vertices = len(graph)
    min_spanning_tree = []  # 存储最小生成树的边

    for u in range(num_vertices):
        for v, weight in graph[u]:
            edges.append((weight, u, v))

    # 根据权重对边进行排序
    edges.sort()

    union_find = UnionFind(num_vertices)

    for weight, u, v in edges:
        if union_find.find(u) != union_find.find(v):
            min_spanning_tree.append((u, v, weight))
            union_find.union(u, v)

    return min_spanning_tree


# 示例图的邻接列表表示（无向图）
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 4), (3, 5)],
    2: [(0, 3), (1, 4), (4, 6)],
    3: [(1, 5)],
    4: [(2, 6)]
}

min_spanning_tree = kruskal(graph)
print("最小生成树的边：", min_spanning_tree)

