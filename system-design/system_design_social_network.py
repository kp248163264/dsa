
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class Graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.graph = [False] * self.nvertices


    def add_edge(self, source, dest):
        newSource = Node(source)
        newDest = Node(dest)

        self.graph[source] = newSource
        newDest.next = self.graph[source]
        self.graph[dest] = newDest
        newSource.next = self.graph[dest]

    def bfs(self, source, dest):
        queue = [self.graph[source]]
        visited = [False] * self.nvertices
        visited[source] = True
        while queue:
            v = queue.pop(0)
            n = self.graph[v.value]
            while n:
                if n.value == dest:
                    return True
                if not visited[n.value]:
                    queue.append(n)
                n = n.next
        return False


    def print_graph(self):
        newline = "\n"
        for i in range(self.nvertices):
            temp = self.graph[i]
            while temp:
                print(f' -> {temp.value}')
                temp = temp.next
            print(f"{newline}")

if __name__ == '__main__':
    edges_to_insert = [(1, 0), (0, 1)]
    g = Graph(2)
    g.add_edge(1,0)
    g.add_edge(0,1)
    g.bfs(1,0)
