# IMPORTS
from collections import defaultdict


# MERGE SORT
def remove_first_entry_of_dict(d):
	"""
	This function removes, by popping, the first element in a Python dictionary
	"""
	key = next(iter(d))
	value = d[key]
	d.pop(next(iter(d)))
	return [key, value]

def merge(d_1, d_2):
	"""
	This function is one part of an implementation of mergesort for Python dictionaries
	"""
	# create the return object 
	d_return = {}
	# get the latest stop until one dict is empty
	while len(d_1) > 0 and len(d_2) > 0:
		# create the traverse objects
		key_1, key_2 = next(iter(d_1)), next(iter(d_2))
		# put the lowest time in first
		if d_1[key_1] < d_2[key_2]:
			d_return[key_1] = d_1[key_1]
			del d_1[key_1]
		else:
			d_return[key_2] = d_2[key_2]
			del d_2[key_2]
	# add remaining elements
	while len(d_1) > 0:
		item = next(iter(d_1))
		d_return[item] = d_1[item]
		del d_1[item]
	while len(d_2) > 0:
		item = next(iter(d_2))
		d_return[item] = d_2[item]
		del d_2[item]
	# return
	return d_return

def merge_sort(d_return):
	"""
	This function is the second part of an implementation of mergesort for Python dictionaries
	"""
	# objects
	d_1 = {}
	d_2 = {}
	length = len(d_return)
	middle = int(length / 2)

	# split the data into two parts
	if len(d_return) > 1:
		for i in range(0, middle, 1):
			next_item = next(iter(d_return))
			d_1[next_item] = d_return[next_item]
			del d_return[next_item]
		for i in range(middle, length, 1):
			next_item = next(iter(d_return))
			d_2[next_item] = d_return[next_item]
			del d_return[next_item]
		# recursion
		d_1 = merge_sort(d_1)
		d_2 = merge_sort(d_2)
		# sorting
		d_return = merge(d_1, d_2)
	# return
	return d_return


# D_GRAPH
def add_to_graph(d_graph, x, y, r):
	# d_graph[x][y]
	if y in d_graph[x]:
		d_graph[x][y] = min(d_graph[x][y], r)
	else:
		d_graph[x][y] = r
	# d_graph[y][x]
	if x in d_graph[y]:
		d_graph[y][x] = min(d_graph[y][x], r)
	else:
		d_graph[y][x] = r

def sort_connections(d_graph):
	for x in d_graph:
		d_graph[x] = merge_sort(d_graph[x])


# DIJKSTRA
def all_other_nodes(d_graph, s):
	return [x for x in d_graph if x != s]

def find_next_node(d_graph, visited_set, path):
	current_node = path[0][-1]
	for node in d_graph[current_node]:
		if node not in visited_set:
			return node
	return -1

def update_paths(d_graph, visited_set, path_dict, current_path, path_id, current_node):
	for node in d_graph[current_node]:
		if node not in visited_set:
			path_id += 1
			

def dijkstra(d_graph, s, e):
	visited_set = set()
	path_dict = defaultdict(list)
	current_node = s
	path_index = 0
	path_dict[path_index] = [[current_node], 0]
	while e not in visited_set:
		# mark that we've visited
		visited_set.add(current_node)
		# find the next closest node
		next_node = find_next_node(d_graph, visited_set, )




if __name__ == '__main__':

	for case in range(int(input().strip())):
		# create the dictionary
		d_graph = defaultdict(dict)
		# collect the data
		for edge in range(int(input().strip().split()[1])):
			data = [int(x) for x in input().strip().split()]
			add_to_graph(d_graph, data[0], data[1], data[2])
		# get the starting point
		s = int(input().strip())
		# sort d_graph
		sort_connections(d_graph)


	
	# # generate the graph
	# d_graph = defaultdict(dict)
	# print(d_graph)
	# print("")

	# add_to_graph(d_graph, 1, 2, 3)
	# print(d_graph)
	# print("")

	# add_to_graph(d_graph, 1, 2, 2)
	# print(d_graph)
	# print("")