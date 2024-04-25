class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])

    def union(self, item1, item2):
        self.parent[self.find(item1)] = self.find(item2)


def kruskal(graph):
    mst = []
    min_cost = 0
    disjoint_set = DisjointSet(graph['vertices'])
    edges = sorted(graph['edges'], key=lambda x: x[2])

    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            mst.append(edge)
            disjoint_set.union(vertex1, vertex2)
            min_cost += weight

    return mst, min_cost


def main():
    num_vertices = int(input("Enter the number of vertices: "))
    vertices = [input(f"Enter vertex {i + 1}: ") for i in range(num_vertices)]

    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for i in range(num_edges):
        vertex1, vertex2, weight = input(f"Enter edge {i + 1} (vertex1 vertex2 weight): ").split()
        edges.append((vertex1, vertex2, int(weight)))

    graph = {
        'vertices': vertices,
        'edges': edges
    }

    mst, min_cost = kruskal(graph)
    
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
    print("Minimum Cost:", min_cost)


if __name__ == "__main__":
    main()



'''
OUTPUT:
Enter the number of vertices: 4
Enter vertex 1: a
Enter vertex 2: b
Enter vertex 3: c
Enter vertex 4: d
Enter the number of edges: 5
Enter edge 1 (vertex1 vertex2 weight): a b 1
Enter edge 2 (vertex1 vertex2 weight): a c 2
Enter edge 3 (vertex1 vertex2 weight): b c 3
Enter edge 4 (vertex1 vertex2 weight): b d 4
Enter edge 5 (vertex1 vertex2 weight): c d 5
Minimum Spanning Tree:
('a', 'b', 1)
('a', 'c', 2)
('b', 'd', 4)
Minimum Cost: 7

=== Code Execution Successful ==='''