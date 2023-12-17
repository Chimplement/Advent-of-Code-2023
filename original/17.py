import math

with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

LEFT = 0
RIGHT = 2
UP = 1
DOWN = 3

def is_in_bounds(map : list[str], cell : tuple[int, int]) -> bool:
	if cell[1] < 0:
		return False
	if cell[1] >= len(map):
		return False
	if cell[0] < 0:
		return False
	if cell[0] >= len(map[0]):
		return False
	return True

MAX_DIR = 10
MIN_DIR = 4

def get_best_route(map : list[str], start_x : int, start_y : int, goal_x : int, goal_y : int) -> int:
	seen = set()
	tentave_distance = {}
	tentave_distance[(start_x, start_y, -1, 0)] = 0
	current = (start_x, start_y, -1, 0)
	possible_current_nodes = set()
	while current != None:
		seen.add(current)
		x, y, last_dir, run = current
		if (x == goal_x and y == goal_y and run >= MIN_DIR):
			return tentave_distance[(x, y, last_dir, run)]
		for dir in (1, 0, RIGHT), (-1, 0, LEFT), (0, 1, DOWN), (0, -1, UP):
			dir_x, dir_y, dir_dir = dir
			if (dir_dir == last_dir and run >= MAX_DIR - 1):
				continue
			if ((dir_dir + 2) % 4 == last_dir):
				continue
			if (run < MIN_DIR - 1 and dir_dir != last_dir and last_dir != -1):
				continue
			check_node = (x + dir_x, y + dir_y)
			if not is_in_bounds(map, check_node):
				continue
			full_node = (check_node[0], check_node[1], dir_dir, 0 if dir_dir != last_dir else run + 1)
			if (full_node in seen):
				continue
			if (full_node in tentave_distance):
				tentave_distance[full_node] = min(tentave_distance[full_node], tentave_distance[(x, y, last_dir, run)] + int(map[check_node[1]][check_node[0]]))
			else:
				tentave_distance[full_node] = tentave_distance[(x, y, last_dir, run)] + int(map[check_node[1]][check_node[0]])
			possible_current_nodes.add(full_node)
		current = None
		lowest_distance = math.inf
		for node in possible_current_nodes:
			if tentave_distance[node] < lowest_distance:
				current = node
				lowest_distance = tentave_distance[node]
		possible_current_nodes.remove(current)
	return (min([tentave_distance[key] for key in tentave_distance if key[0] == goal_x and key[1] == goal_y]))

print(get_best_route(input_lines, 0, 0, len(input_lines[0]) - 1, len(input_lines) - 1))