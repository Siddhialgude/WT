class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def is_safe(self, v, color, colored_nodes):
        for i in range(self.vertices):
            if self.adj_matrix[v][i] == 1 and colored_nodes[i] == color:
                return False
        return True

    def graph_coloring_util(self, m, colored_nodes, v):
        if v == self.vertices:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, c, colored_nodes):
                colored_nodes[v] = c
                if self.graph_coloring_util(m, colored_nodes, v + 1):
                    return True
                colored_nodes[v] = 0

        return False

    def graph_coloring(self, m, color_names):
        colored_nodes = [0] * self.vertices
        if not self.graph_coloring_util(m, colored_nodes, 0):
            print("No solution exists.")
            return False

        print("One possible solution:")
        for i in range(self.vertices):
            print("Node", i, "is colored with", color_names[colored_nodes[i] - 1])
        return True

# Example usage:
vertices = int(input("Enter the number of vertices: "))
adj_matrix = []
print("Enter the adjacency matrix (row-wise):")
for _ in range(vertices):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

colors = int(input("Enter the number of colors: "))
color_names = input("Enter the color names separated by space: ").split()

g = Graph(vertices)

for i in range(vertices):
    for j in range(vertices):
        if adj_matrix[i][j] == 1:
            g.add_edge(i, j)

g.graph_coloring(colors, color_names)
'''
OUTPUT:
Enter the number of vertices: 4
Enter the adjacency matrix (row-wise):
0 1 1 1
1 0 0 1
1 0 0 1
1 1 1 0
Enter the number of colors: 4
Enter the color names separated by space: R G B Y
One possible solution:
Node 0 is colored with R
Node 1 is colored with G
Node 2 is colored with G
Node 3 is colored with B
'''