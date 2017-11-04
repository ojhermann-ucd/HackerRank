# COMMENTS
"""
Works, but terminates due to timeout 4 through 7
"""

# IMPORT


# GRAPH
def create_graph(N):
	return [[100001] * N for n in range(N)]

def update_graph(graph, x, y, r):
	x -= 1
	y -= 1
	graph[x][y] = min(graph[x][y], r)
	graph[y][x] = min(graph[y][x], r)


# DIJKSTRA'S ALGORITHM
def update_path_list(graph, visited_set, path_dict, node, N):
	# source data
	node = min(path_dict, key=path_dict.get)
	distance = path_dict[node]
	del path_dict[node]
	# update visted_set
	visited_set.add(node)
	# destination data
	possible_nodes = [n for n in range(N) if n not in visited_set]
	for possible_node in possible_nodes:
		if graph[node][possible_node] < 100001:
			if possible_node in path_dict:
				path_dict[possible_node] = min(path_dict[possible_node], distance + graph[node][possible_node])
			else:
				path_dict[possible_node] = distance + graph[node][possible_node]

def dijkstra(graph, N, start, end):
	start -= 1
	end -= 1
	visited_set = set()
	path_dict = dict()
	path_dict[start] = 0
	node = start
	while len(path_dict) > 0:
		node = min(path_dict, key=path_dict.get)
		distance = path_dict[node]
		if node == end:
			return distance
		update_path_list(graph, visited_set, path_dict, node, N)
	return -1


# if __name__ == '__main__':

# 	solutions = list()

# 	for test_case in range(int(input().strip())):
# 		parameters = [int(x) for x in input().strip().split()]
# 		number_of_nodes, number_of_edges = parameters[0], parameters[1]
# 		this_graph = create_graph(number_of_nodes)
# 		for connection in range(number_of_edges):
# 			data = [int(x) for x in input().strip().split()]
# 			update_graph(this_graph, data[0], data[1], data[2])
# 		start = int(input().strip())
# 		temp_solutions = list()
# 		for end in range(1, number_of_nodes + 1):
# 			if end != start:
# 				temp_solutions.append(dijkstra(this_graph, number_of_nodes, start, end))
# 		solutions.append([str(x) for x in temp_solutions])

# 	for item in solutions:
# 		print(" ".join(item))


# test_graph = [ 
# 	[100001, 24, 3, 20], 
# 	[24, 100001, 100001, 100001], 
# 	[3, 100001, 100001, 12], 
# 	[20, 100001, 12, 100001] 
# 	]

# print(dijkstra(test_graph, 4, 1, 2))
# print(dijkstra(test_graph, 4, 1, 3))
# print(dijkstra(test_graph, 4, 1, 4))
# print("")
# print(dijkstra(test_graph, 4, 2, 1))
# print(dijkstra(test_graph, 4, 2, 3))
# print(dijkstra(test_graph, 4, 2, 4))




if __name__ == '__main__':

	solutions = list()

	with open("input.hacker", "r") as source:
		test_cases = int(source.readline())
		# print("test_cases: {}".format(test_cases))
		for t in range(test_cases):
			parameters = [int(x) for x in source.readline().strip().split()] 
			number_of_nodes, number_of_edges = parameters[0], parameters[1]
			# print("nodes, edges: {}, {}".format(number_of_nodes, number_of_edges))
			this_graph = create_graph(number_of_nodes)
			for connection in range(number_of_edges):
				data = [int(x) for x in source.readline().strip().split()]
				update_graph(this_graph, data[0], data[1], data[2])
			start = int(source.readline().strip())
			temp_solutions = list()
			for end in range(1, number_of_nodes + 1):
				if end != start:
					temp_solutions.append(dijkstra(this_graph, number_of_nodes, start, end))
			solutions.append([str(x) for x in temp_solutions])

	answers = list()
	with open("output.hacker", "r") as source:
		for line in source:
			answers.append(line.strip().split())

	count = 0
	for s in solutions:
		if s == answers[count]:
			print("OK for {}".format(count))
			print("")
		else:
			print("Not OK for {}".format(count))
			print(s)
			print(answers[count])
			sub_count = 0
			for item in s:
				if item != answers[count][sub_count]:
					print(item, answers[count][sub_count], sub_count)
				sub_count += 1
			print("")
		count += 1

