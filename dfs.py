from structure.graph.adjListGraph import Graph

def dfsvisit(startVertex):
    startVertex.setColor('gray')
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsvisit(nextVertex)
    print(startVertex.id)
    startVertex.setColor('black')


g = Graph()
a = g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');
g.addVertex('F');
g.addVertex('G');
g.addVertex('H');
g.addVertex('I');

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('A', 'F')
g.addEdge('A', 'G')

g.addEdge('B', 'A')
g.addEdge('B', 'D')
g.addEdge('B', 'E')

g.addEdge('C', 'A')
g.addEdge('C', 'E')
g.addEdge('C', 'G')
g.addEdge('C', 'I')

g.addEdge('D', 'A')
g.addEdge('D', 'B')

g.addEdge('E', 'B')
g.addEdge('E', 'C')

g.addEdge('F', 'A')

g.addEdge('G', 'A')
g.addEdge('G', 'C')
g.addEdge('G', 'H')

g.addEdge('H', 'G')

g.addEdge('I', 'C')

dfsvisit(a)