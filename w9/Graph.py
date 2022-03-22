from collections import deque


class Node:
    # creates a node
    def __init__(self, i):
        self.id = i
        
class Graph:
    # creates a graph
    def __init__(self):
        self.n = 0      # Number of vertices
        self.V = []     # Vertices
        self.Adj = []   # Adjacency list
    
    # add a node
    def add_node(self):
        node = Node(self.n)
        self.n = self.n+1
        self.V.append(node)
        self.Adj.append(deque())        
        return node
        
    # get node with id
    def get_node(self, vid):
        node = None
        for v in self.V:
            if v.id == vid:
                node = v
                break
        return node
    
    # add weighted undirected edge
    def add_weighted_edge(self, u, v, w):
        self.Adj[u.id].append((v,w))
        self.Adj[v.id].append((u,w))
        
    # add weighted undirected edge
    def add_weighted_directed_edge(self, u, v, w):
        self.Adj[u.id].append((v,w))
        
    # display graph itself      
    def display(self):
        for i in range(0,self.n):
            s = ""
            for v,w in self.Adj[i]:
                s = "(" + str(v.id) + "," + str(w) + ")" + " " + s
            s = str(i) + ": " + s
            print(s)
        
if __name__ == '__main__':
    G = Graph()
    v0 = G.add_node()
    v1 = G.add_node()
    v2 = G.add_node()
    v3 = G.add_node()
    G.add_weighted_edge(v0,v1,1)
    G.add_weighted_edge(v1,v2,2)
    G.add_weighted_edge(v2,v3,3)
    G.add_weighted_edge(v3,v0,4)
    
    G.display()
    
    # This is the first vertex in the adjacency list of v0 
    # (a Node object)
    print(G.Adj[0][0][0])
    # And this is the weight of the edge from v0 to this vertex
    # (an integer)
    print(G.Adj[0][0][1])
