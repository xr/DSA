from structure.graph.adjListGraph import Graph, Vertex
from structure.heap.binheap import BinHeap


Q = BinHeap()

result = []
visited = []

def dijkstra(g, root):
	for u in g:
		u.priority = 10000
		u.unvisited = True
		u.father = None
	root.priority = 0
	Q.insert(root.priority, root)
	while Q.currentSize:
		u = Q.delMin()['data']
		visited.append(u.id)
		if (u.father, u) not in result:
			if u.father:
				print((u.father.id, u.id))
			else:
				print((u.father, u.id))
			result.append((u.father, u))
		for v in u.getConnections():
			if (v.id not in visited) and (u.priority + u.getWeight(v)) < v.priority:
				v.father = u
				v.priority = u.getWeight(v) + u.priority
				Q.insert(v.priority, v)


g = Graph()

g.addEdge('a', 'b', 8)
g.addEdge('a', 'g', 4)
g.addEdge('a', 'j', 14)

g.addEdge('b', 'a', 8)
g.addEdge('b', 'e', 1)
g.addEdge('b', 'f', 14)

g.addEdge('c', 'd', 13)
g.addEdge('c', 'f', 10)
g.addEdge('c', 'g', 6)

g.addEdge('d', 'c', 13)
g.addEdge('d', 'f', 14)
g.addEdge('d', 'h', 4)

g.addEdge('e', 'b', 1)
g.addEdge('e', 'g', 9)
g.addEdge('e', 'h', 8)

g.addEdge('f', 'b', 14)
g.addEdge('f', 'c', 10)
g.addEdge('f', 'd', 14)

g.addEdge('g', 'a', 4)
g.addEdge('g', 'c', 6)
g.addEdge('g', 'e', 9)
g.addEdge('g', 'j', 2)

g.addEdge('h', 'd', 4)
g.addEdge('h', 'e', 8)
g.addEdge('h', 'j', 14)

g.addEdge('j', 'a', 14)
g.addEdge('j', 'g', 2)
g.addEdge('j', 'h', 14)

root = g.getVertex('a')

dijkstra(g, root)
