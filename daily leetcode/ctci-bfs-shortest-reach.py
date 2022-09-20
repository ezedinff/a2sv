'''
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
'''

from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def connect(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def find_all_distances(self, start):
        distances = [-1] * self.n
        distances[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 6
                    queue.append(neighbor)
        print(' '.join(map(str, distances[:start] + distances[start+1:])))



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = Graph(n)
        for _ in range(m):
            x, y = map(int, input().split())
            graph.connect(x-1, y-1)
        start = int(input())
        graph.find_all_distances(start-1)