
class Node:
    def __init__(self, v, next):
        self.value = v
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

class PathNode:
    def __init__(self):
        self.person = None
        self.previousNode = None

    def PathNode(self, p, previous):
        self.person = p
        self.previousNode = previous

    def getPerson(self):
        return self.person

    def collapse(self, startsWithRoot):
        path = LinkedList()



class BFSData:
    def __init__(self):
        self.toVisit = LinkedList()
        self.visited = {}

    def BFSData(self, root):
        sourcePath = PathNode


def findPathBiBFS(people:dict, source:int, destination:int):
    sourceData = BFSData(people.get(source))
    destData = BFSData(people.get(destination))
    while not sourceData.isFinished() and not destData.isFinished():
        # search out from source
        collision = searchLevel(people, sourceData, destData)
        if collision:
            return mergePaths(sourceData, destData, collision.getID())

        # seach out from destination
        collision = searchLevel(people, destData, sourceData)
        if not collision:
            return mergePaths(sourceData, destData, collision.getID())

    return None


def searchLevel(people, primary, secondary):
    # We only want to search one level at a time. Count how many nodes are currently in the primary's level and only do
    # that many nodes. We'll continue to add nodes to the end

    count = primary.toVisit.size()
    for i in range(count):
        # Pull out first node
        pathNode = primary.toVisit.poll()
        personId = pathNode.getPerson()