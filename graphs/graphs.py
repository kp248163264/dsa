
class Node:
    def __init__(self, y, weight, next):
        self.y = y
        self.weight = weight
        self.next = next

class AdjacencyListGraph:
    def __init__(self, max_vertices, nvertices=0, nedges=0, directed=True):
        self.max_vertices = max_vertices
        self.edges = [None] * (self.max_vertices+1)
        self.degrees = [0] * (self.max_vertices+1) # out-degrees of each node
        self.nvertices = nvertices # number of vertices in graph
        self.nedges = nedges # number of edges in graph
        self.directed = directed

    def insert_edge(self, g,x,y,directed):
        # insert y before x
        y_node = Node(y,None, g.edges[x])
        g.edges[x] = y_node
        g.degrees[x] +=1
        if not directed:
            self.insert_edge(g,y,x,True)
        else:
            g.nedges+=1

    def print_graph(self, g):
        for i in range(g.nvertices):
            nl = '\n'
            print(f'{i}: ')
            p = g.edges[i]
            while p:
                print(f'{p.y}')
                p = p.next
            print(f'{nl}')

    def insert_edges(self, directed, edges_to_insert):
        MAX_V = 1000
        g = AdjacencyListGraph(MAX_V, nvertices=len(edges_to_insert))
        for (x,y) in edges_to_insert:
            self.insert_edge(g,x,y,directed)
        self.print_graph(g)

    def process_vertex_early(self, v):
        print(f"processed vertex: {v.y}")

    def process_edge(self, u, y):
        self.nedges+=1
        print(f"processed edge: {u}, {y}")

    def process_vertex_late(self, u):
        print(f"processed vertex: {u}")


    def bfs(self, g, s):
        discovered = [False] * g.nvertices
        processed = [False] * g.nvertices
        parents = [False] * g.nvertices
        queue = [s]
        discovered[s] = True
        while len(queue) > 0:
            u = queue.pop(0)
            self.process_vertex_early(u)
            processed[u] = True
            # process vertex u as desired
            p = g.edges[u]
            while p:
                y = p.y
                if processed[y] == False or g.directed:
                    # process edge (u, v) as desired
                    self.process_edge(u,y)
                if not discovered[y]:
                    queue.append(y)
                    discovered[y] = True
                    parents[y] = u
                p = p.next
            self.process_vertex_late(u)
            state[u] = "p"

def bfs_two_states(g,s):

    # g = graph - stored as dictionary, where key is node, value is list of neighbors
    # s = target node

    visited = [False] * g.nvertices
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        for i in g[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def bfs_three_states(g,s):

    v_status = [-1] * g.nvertices
    queue = [s]
    while queue:
        p = queue.pop(0)
        v_status[p] = 0
        for n in g[p]:
            if v_status[n] == -1:
                queue.append(n)
        v_status[p] = 1




def route_between_nodes(self, n1:Node, n2:Node, g):
    """Given a directed graph, design an algorithm to find out whether there is a route between
    two nodes, n1 & n2."""
    v_status = [-1] * g.nvertices
    queue = [n1]
    while queue:
        p = queue.pop(0)
        for n in g[p]:
            if v_status[n] == -1:
                if n == n2:
                    return True
                else:
                    v_status[n] = 0
                    queue.append(n)
        v_status[p] = 1
    return False


if __name__ == '__main__':
    edges_to_insert = [(1,0), (0,1)]
    insert_edges(True, edges_to_insert)

