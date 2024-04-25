class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = [False] * self.vertices

        print(start, end=' ')
        visited[start] = True

        for i in range(self.vertices):
            if self.adj_matrix[start][i] == 1 and not visited[i]:
                self.dfs_recursive(i, visited)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = [start]
        visited[start] = True

        while queue:
            current = queue.pop(0)
            print(current, end=' ')

            for i in range(self.vertices):
                if self.adj_matrix[current][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True


# Taking input from the user in the form of edges
num_edges = int(input("Enter the number of edges: "))
num_vertices = int(input("Enter the number of vertices: "))
graph_bfs = Graph(num_vertices)
graph_dfs = Graph(num_vertices)

print("Enter the edges (u v) separated by space:")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph_bfs.add_edge(u, v)
    graph_dfs.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for traversal: "))

print("DFS Recursive:")
graph_dfs.dfs_recursive(start_vertex)
print()

print("BFS:")
graph_bfs.bfs(start_vertex)
'''
OUTPUT:

Enter the number of edges: 7
Enter the number of vertices: 5
Enter the edges (u v) separated by space:
0 1
1 4
4 3
3 2
2 0
1 3
2 4
Enter the starting vertex for traversal: 3
DFS Recursive:
3 1 0 2 4 
BFS:
3 1 2 4 0

'''














