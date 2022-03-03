from collections import deque
from platform import node


class Node:
    def __init__(self, id):
        self.id = id


class Graph:
    def __init__(self):
        self.V = []
        self.Adj = []
        self.n = 0

    def add_node(self):
        node = Node(self.n)
        self.n += 1
        self.V.append(node)
        self.Adj.append(deque())
        return node

    def get_node(self, node_id):
        for node in self.V:
            if node.id == node_id:
                return node
        return None

    def add_edge(self, u_node: Node, v_node: Node):
        self.Adj[u_node.id].append(v_node)
        self.Adj[v_node.id].append(u_node)

    def add_edge_using_ids(self, u_id, v_id):
        u_node = self.get_node(u_id)
        v_node = self.get_node(v_id)
        self.add_edge(u_node, v_node)
