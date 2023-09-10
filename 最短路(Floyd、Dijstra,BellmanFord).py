# Floyd算法:
import numpy
import numpy as np


def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = graph.copy()

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# 示例图的邻接矩阵
graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

result = floyd_warshall(graph)
print(np.array(result))

import heapq


def dijkstra(graph, start):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start] = 0
    visited = [False] * num_vertices

    pq = [(0, start)]

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True

        for neighbor, weight in enumerate(graph[current_vertex]):
            if not visited[neighbor] and weight > 0:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return dist


# 示例图的邻接矩阵
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

result = dijkstra(graph, 0)
print(result)


def bellman_ford(graph, start):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start] = 0

    for _ in range(num_vertices - 1):
        for u, v, weight in graph:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for u, v, weight in graph:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("图中存在负权环路")
            return

    return dist


# 示例图的边列表（有向图）
graph = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, 5),
    (1, 3, 10),
    (2, 3, 3),
    (3, 0, 7),
    (3, 4, 2),
    (4, 3, 4),
    (4, 1, 3)
]

result = bellman_ford(graph, 0)
print(result)



