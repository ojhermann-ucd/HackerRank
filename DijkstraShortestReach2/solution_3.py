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
def pop_minimum_value(path_list):
	the_index = path_list.index(min(path_list, key=itemgetter(1)))
	return path_list.pop(the_index)

def create_path_list(graph, start, N, visited_set):
	visited_set.add(start)
	path_list = list()
	for j in range(N):
		if graph[start - 1][j] != 100001:
			path_list.append([ [start, j+1], graph[start - 1][j] ])
	# sort path_list
	path_list.sort(key=lambda x: x[1])
	return path_list

def extend_path(graph, path_list, visited_set, N, end):
	path_details = path_list.pop(0)
	path = path_details[0]
	node = path[-1]
	distance = path_details[1]
	if node == end:
		return [True, distance]
	for possible_node in range(N):
		if (possible_node + 1) not in visited_set and graph[node - 1][possible_node] < 100001:
			path_list.append([ path + [possible_node + 1], distance + graph[node - 1][possible_node] ])
	# update visited_set
	visited_set.add(node)
	# sort path_list
	path_list.sort(key=lambda x: x[1])
	# return
	return [False, -1]

def dijkstra(graph, start, end, N):
	visited_set = set()
	path_list = create_path_list(graph, start, N, visited_set)
	path = [False, -1]
	while not path[0] and len(path_list) > 0:
		path = extend_path(graph, path_list, visited_set, N, end)
	return path[1]


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
					temp_solutions.append(dijkstra(this_graph, start, end, number_of_nodes))
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



	

	# for test_case in range(int(input().strip())):
	# 	parameters = [int(x) for x in input().strip().split()]
	# 	number_of_nodes, number_of_edges = parameters[0], parameters[1]
	# 	this_graph = create_graph(number_of_nodes)
	# 	for connection in range(number_of_edges):
	# 		data = [int(x) for x in input().strip().split()]
	# 		update_graph(this_graph, data[0], data[1], data[2])
	# 	start = int(input().strip())
	# 	temp_solutions = list()
	# 	for end in range(1, number_of_nodes + 1):
	# 		if end != start:
	# 			temp_solutions.append(dijkstra(this_graph, start, end, number_of_nodes))
	# 	solutions.append([str(x) for x in temp_solutions])

	# for item in solutions:
	# 	print(" ".join(item))