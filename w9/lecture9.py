from collections import deque
from math import inf
from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, n):
        self.id = n
        self.pi = None
        self.d = inf  # replace with self.key for prims
        self.pos = inf
        self.inQueue = True


class Graph:
    def __init__(self):
        self.n = 0
        self.V = []
        self.Adj = []

    def add_node(self):
        new_node = Node(self.n)
        self.n += 1
        self.V.append(new_node)
        self.Adj.append(deque())
        return new_node

    def get_node(self, id):
        for v in self.V:
            if v.id == id:
                return v
        return None

    # represents edge from u to v with weight w
    def add_weighted_directed_edge(self, u, v, w):
        self.Adj[u.id].append((v, w))

    def add_weighted_edge(self, u, v, w):
        self.add_weighted_directed_edge(u, v, w)
        self.add_weighted_directed_edge(v, u, w)

    def display_edges(self):
        for v in self.V:
            s = f'Node {v.id}: '
            for u, w in self.Adj[v.id]:
                s += f'({u.id}, {w}) '
            print(s)

    def display_previous(self):
        for v in self.V:
            if v.pi == None:
                print(v.id, None)
            else:
                print(v.id, v.pi.id)


def swap(Q, i, j):
    """
    Swaps the two nodes based on indices.

    Input:
        Q: Min-heap (list)
        i: indices to swap
        j: indices to swap
    """
    Q[i], Q[j] = Q[j], Q[i]
    Q[i].pos = i
    Q[j].pos = j


def minHeapify(Q, i):
    """
    Runs min-heapify on an index

    Input:
        Q: Min-heap (list)
        i: index
    """
    l = 2*i + 1
    r = 2*i + 2
    smallest = i
    for c in [l, r]:
        if c < len(Q) and Q[c].d < Q[smallest].d:
            smallest = c
    if smallest == i:
        return
    else:
        swap(Q, i, smallest)
        minHeapify(Q, smallest)


def extractMin(Q) -> Node:
    """
    Extracts the minimum value out of priority Queue

    Input:
        Q: Min-heap (list)

    Returns:
        v: node with minimum key value (Node)
    """
    swap(Q, 0, len(Q) - 1)
    min_node = Q.pop()
    minHeapify(Q, 0)
    return min_node


def decreaseKey(Q, u: Node, k):
    """
    Decreases the key of a node an updates the priority Queue

    Input:
        Q: min-heap (list)
        u: node to be updated (node)
        k: new lower key (int)
    """
    if k >= u.d:
        raise ValueError("Key value not lower than original")
    u.d = k
    i = u.pos
    while i > 0 and Q[i].d < Q[(i-1)//2].d:
        swap(Q, i, (i-1)//2)
        i = (i-1)//2


def insert(Q, u: Node, k):
    """
    Inserts a node wit certain key value

    Input:
        Q: min-heap (list)
        u: node to be inserted (Node)
        k: distance value (int)
    """
    u.d = inf
    u.pos = len(Q)
    Q.append(u)
    decreaseKey(Q, u, k)


def dijkstra(G: Graph, s: Node):
    """
    Runs dijkstras on graph with source vertex s.

    Input:
        G: (graph) see above
        s: source vertex (node)

    Returns: 
        A list of tuples containing id of nodes and distances

    """
    Q = []
    for i in range(len(G.V)):
        u = G.V[i]
        u.d = inf
        u.pos = i
        u.pi = None
        u.inQueue = True
        Q.append(u)
    decreaseKey(Q, s, 0)
    while Q:
        u = extractMin(Q)
        u.inQueue = False
        for v, w in G.Adj[u.id]:
            # replace u.d + w < v.d
            # with w < v.d to get prim's algorithm
            if v.inQueue and u.d + w < v.d:
                v.pi = u
                decreaseKey(Q, v, u.d + w)

    return [f'{u.id}, {u.d}' for u in G.V]


if __name__ == '__main__':

    # Example graph from CLRS 24.3
    G = Graph()
    s = G.add_node()
    t = G.add_node()
    y = G.add_node()
    x = G.add_node()
    z = G.add_node()

    G.add_weighted_directed_edge(s, t, 10)
    G.add_weighted_directed_edge(s, y, 5)
    G.add_weighted_directed_edge(t, x, 1)
    G.add_weighted_directed_edge(t, y, 2)
    G.add_weighted_directed_edge(x, z, 4)
    G.add_weighted_directed_edge(y, t, 3)
    G.add_weighted_directed_edge(y, x, 9)
    G.add_weighted_directed_edge(y, z, 2)
    G.add_weighted_directed_edge(z, x, 6)
    G.add_weighted_directed_edge(z, t, 7)

    # Print graph
    print("Example graph:")
    G.display_edges()

    # Run Prim's algorithm
    print(dijkstra(G, s))

    print("")

    print("The distances are:")
    for v in G.V:
        print(v.id, v.d)
