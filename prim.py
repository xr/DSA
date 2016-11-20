from structure.graph.adjListGraph import Graph, Vertex
from structure.heap.binheap import BinHeap


# NOTE: the prim function has some bug that do not track the closed list
# based on http://www.cse.hut.fi/en/research/SVG/TRAKLA2/exercises/Prim-27.html

Q = BinHeap()

result = []

def prim(g, root):
	for u in g:
		u.priority = 10000
		u.unvisited = True
		u.father = None
	root.priority = 0
	Q.insert(root.priority, root)
	while Q.currentSize:
		u = Q.delMin()['data']
		u.unvisited = False
		if u.father:
			print((u.father.id, u.id))
		else:
			print((u.father, u.id))
		result.append((u.father, u))
		for v in u.getConnections():
			print(v.id, v.unvisited)
			if v.unvisited and u.getWeight(v) < v.priority:
				v.father = u
				v.priority = u.getWeight(v)
				Q.insert(v.priority, v)



g = Graph()

g.addEdge('a', 'b', 3)
g.addEdge('a', 'c', 4)
g.addEdge('a', 'e', 11)
g.addEdge('a', 'h', 13)
g.addEdge('a', 'j', 15)

g.addEdge('b', 'a', 3)
g.addEdge('b', 'c', 10)
g.addEdge('b', 'd', 5)
g.addEdge('b', 'f', 12)
g.addEdge('b', 'g', 14)

g.addEdge('c', 'a', 4)
g.addEdge('c', 'b', 10)
g.addEdge('c', 'e', 2)
g.addEdge('c', 'g', 8)

g.addEdge('d', 'b', 5)
g.addEdge('d', 'e', 6)
g.addEdge('d', 'f', 7)
g.addEdge('d', 'g', 15)

g.addEdge('e', 'a', 11)
g.addEdge('e', 'c', 2)
g.addEdge('e', 'd', 6)
g.addEdge('e', 'h', 9)

g.addEdge('f', 'b', 12)
g.addEdge('f', 'd', 7)

g.addEdge('g', 'b', 14)
g.addEdge('g', 'c', 8)
g.addEdge('g', 'd', 15)

g.addEdge('h', 'a', 13)
g.addEdge('h', 'e', 9)
g.addEdge('h', 'j', 1)

g.addEdge('j', 'a', 15)
g.addEdge('j', 'h', 1)

root = g.getVertex('a')

prim(g, root)
