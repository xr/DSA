from structure.graph.adjListGraph import Graph, Vertex
from structure.linear.queue import Queue


def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    print(currentVert.id)
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


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


for k in a.getConnections():
	print(k.id)
bfs(g, a)