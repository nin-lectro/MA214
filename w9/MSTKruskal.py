from Graph import Graph


# Kruskal's algorithm
# Output a list of edges of an MST
# Each edge indicated as (u,v,w) where u and v are the vertices,
# w is the weight of the edge
def MSTKruskal(G):
    A = []
    # set the parents of forest for discrete set data structure
    parent = [i for i in range(len(G.V))]
    # extract all the edges
    edges = [(u, v, w) for u in G.V for v, w in G.Adj[u.id]]
    # sort by weight
    edges.sort(key=lambda tuple: tuple[2])
    # choose safe edges
    for u, v, w in edges:
        # can break here as MST must have V - 1 edges
        if len(A) == len(G.V) - 1:
            break
        # check if in the same set
        if find(parent, u.id) != find(parent, v.id):
            union(parent, u.id, v.id)
            A.append((u, v, w))
    return A


def find(parent, i):
    # implement the find-set from textbook
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])


def union(parent, i, j):
    # sets the union of the two sets
    irep = find(parent, i)
    jrep = find(parent, j)
    parent[irep] = jrep


if __name__ == '__main__':

    # Example graph from CLRS and Lecture
    G = Graph()
    v0 = G.add_node()
    v1 = G.add_node()
    v2 = G.add_node()
    v3 = G.add_node()
    v4 = G.add_node()
    v5 = G.add_node()
    v6 = G.add_node()
    v7 = G.add_node()
    v8 = G.add_node()

    G.add_weighted_edge(v0, v1, 4)
    G.add_weighted_edge(v0, v7, 8)
    G.add_weighted_edge(v1, v2, 8)
    G.add_weighted_edge(v1, v7, 11)
    G.add_weighted_edge(v2, v3, 7)
    G.add_weighted_edge(v2, v5, 4)
    G.add_weighted_edge(v2, v8, 2)
    G.add_weighted_edge(v3, v4, 9)
    G.add_weighted_edge(v3, v5, 14)
    G.add_weighted_edge(v4, v5, 10)
    G.add_weighted_edge(v5, v6, 2)
    G.add_weighted_edge(v6, v7, 1)
    G.add_weighted_edge(v6, v8, 6)

    # Print graph
    print("Example graph:")
    G.display()

    # Run Kruskal's algorithm
    # Output a list of edges of an MST
    # Each edge (u,v,w) where u and v are the vertices,
    # w is the weight of the edge
    T = MSTKruskal(G)

    print("")

    # Print the spanning tree
    print("The edges of the MST found by Kruskal's algorithm:")
    for u, v, w in T:
        print('(', u.id, ',', v.id, '), weight: ', w)
