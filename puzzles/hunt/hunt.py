"""
In this exercise, we’re building a solving algorithm for an old-school back-to-basics computer game. It’s a very simple text based adventure game where you walk around and try to find treasures, while avoiding traps. The game is played on a rectangular, two dimensional grid.

The game will consist of the player moving around on the grid for as long as they like (or until they fall into a trap). The player can move up, down, left and right (but not diagonally). If the player enters a square containing gold, the gold is picked up. If the player stands next to (i.e., immediately up, down, left, or right of) one or more traps, they will "sense a draft" but do not know from what direction the draft comes, or how many traps are near. It is not possible to enter squares which contain walls. Squares which contain walls or traps can never contain gold, i.e. all gold is positioned on normal floor tiles.

For scoring purposes, we want to show the player how much gold they could have gotten safely. That is, how much gold can a player get playing with an optimal strategy and always being sure that the square they walked into was safe.

Specifications

Implement the function safe_gold which accepts one string as a parameter, which represents the played level. The level consists of several rows, which are separated by newlines. The method str.splitlines might be useful.

The level can contain 5 different elements, which are:

P starting position of the player (exactly one for every level)
G piece of gold
T a trap
# a wall
. normal floor
Return value

The function safe_gold should return one integer, which represents the maximum amount of gold pieces the player could have collected for the level given as parameter.
"""

import sys
sys.setrecursionlimit(100000)

# add result in top, right, down, left
directions = [
	(-1, 0),
	(0, 1),
	(1, 0),
	(0, -1)
]
def check_item(str):
	return {
		'.': 'floor',
		'G': 'gold',
		'#': 'wall',
		'T': 'trap',
		'P': 'init'
	}[str];

def find_position(graph):
	max_row = len(graph)
	max_col = len(graph[0])
	for one_dia_index in range(1, max_row - 1):
		for sec_dia_index in range(1, max_col - 1):
			if graph[one_dia_index][sec_dia_index] == 'P':
				return {
					'position': (one_dia_index, sec_dia_index),
					'row_range': (1, max_row - 2),
					'col_range': (1, max_col - 2)
				}

def is_wall(current_position):
	item = check_item(graph[current_position[0]][current_position[1]])
	if item == 'wall':
		return True
	else:
		return False

def is_trap(current_position):
	item = check_item(graph[current_position[0]][current_position[1]])
	if item == 'trap':
		return True
	else:
		return False

def is_out(current_position):
	if out_range(current_position[0], position['row_range']) or out_range(current_position[1], position['col_range']):
		return True
	else:
		return False

def is_gold(current_position):
	item = check_item(graph[current_position[0]][current_position[1]])
	if item == 'gold':
		return True
	else:
		return False

def out_range(num, c_range):
	if num < c_range[0] or num > c_range[1]:
		return True
	else:
		return False

def build_matrix_graph(string):
	one_dia = string.splitlines()
	graph = []

	for item in one_dia:
		graph.append(list(item))

	return graph

def position_str(position):
	return 'x' + str(position[0]) + 'y' + str(position[1])

def is_visited(current_position):
	p_str = position_str(current_position)
	if p_str in visited:
		return True
	else:
		return False

def is_in_queue(position):
	return position in queue

def bfs():
	global queue
	if len(queue):
		current_position = queue.pop(0)
		if is_gold(current_position):
			gold_arr[position_str(current_position)] = True
		visited[position_str(current_position)] = True
		if not is_out(current_position) and not is_wall(current_position):
			has_trap = False
			for item in directions:
				next_position = (item[0] + current_position[0], item[1] + current_position[1])
				if is_trap(next_position):
					has_trap = True

			if not has_trap:
				for item in directions:
					next_position = (item[0] + current_position[0], item[1] + current_position[1])
					if not is_visited(next_position) and not is_wall(next_position) and not is_out(next_position) and not is_in_queue(next_position):
						queue.append(next_position)
		bfs()

def safe_gold(level_string):
    """
    Starting from tile 'P' in level_string, calculate and return the amount of safe gold which can be collected.
    """
    global graph
    global position
    global gold_arr
    global visited
    global queue

    gold = 0
    visited = {}
    queue = []
    gold_arr = {}

    # build graph
    graph = build_matrix_graph(level_string)

    # find start position, col, row proper range
    position = find_position(graph)

    queue.append(position['position'])

    # start bfs
    bfs()

    gold = len(gold_arr)
    
    return gold




# with open("testdata/small.txt") as test_file:
# 	correct_answer = int(test_file.readline().strip())
# 	level = ''.join(test_file.readlines())



# print(safe_gold(level))
