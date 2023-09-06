# Floyd算法:
import numpy

def floyd(graph):
    n=len(graph)
    dist=graph.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j]> dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]



