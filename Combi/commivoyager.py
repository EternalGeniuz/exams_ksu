import numpy as np

def traveling_salesman(graph, start):
    n = len(graph)
    visited = [False] * n
    path = []
    current = start
    total_cost = 0

    for _ in range(n):
        path.append(current)
        visited[current] = True
        next_city = None
        min_cost = float('inf')

        for city in range(n):
            if not visited[city] and graph[current][city] < min_cost:
                min_cost = graph[current][city]
                next_city = city

        if next_city is not None:
            total_cost += min_cost
            current = next_city

    total_cost += graph[current][start]
    path.append(start)
    return path, total_cost

# Пример использования
graph = np.array([[0, 29, 20, 21],
                  [29, 0, 15, 17],
                  [20, 15, 0, 28],
                  [21, 17, 28, 0]])
start = 0
path, cost = traveling_salesman(graph, start)
print(f"Path: {path}, Cost: {cost}")
