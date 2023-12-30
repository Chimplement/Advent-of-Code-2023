import functools

with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

def is_path(map, cell):
	x, y = cell
	if y < 0 or x < 0:
		return False
	if y >= len(map) or x >= len(map[y]):
		return False
	return map[y][x] != '#'

def get_dirs(tile):
	# if tile == '>':
	# 	return [(1, 0)]
	# if tile == '<':
	# 	return [(-1, 0)]
	# if tile == 'v':
	# 	return [(0, 1)]
	# if tile == '^':
	# 	return [(0, -1)]
	return [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_choices(map, cell, visited):
	x, y = cell
	if y < 0 or x < 0:
		return []
	if y >= len(map) or x >= len(map[y]):
		return []
	return tuple((dir_x, dir_y) for dir_x, dir_y in get_dirs(map[y][x]) if is_path(map, (x + dir_x, y + dir_y)) and not (x + dir_x, y + dir_y) in visited)

def follow_path(map, frm, current_choices):
	x, y = frm
	path_lenght = 0
	visited = (x, y),
	while len(current_choices) == 1:
		dir_x, dir_y = current_choices[0]
		x, y = (x + dir_x, y + dir_y)
		visited = *visited, (x, y)
		path_lenght += 1
		current_choices = get_choices(map, (x, y), visited)
	return (x, y, path_lenght, current_choices, visited)

@functools.lru_cache(maxsize=None)
def get_longest_path(map, frm, to, visited = None):
	if visited == None:
		visited = ()
	if frm == to:
		return 0
	visited = *visited, frm
	x, y = frm

	current_choices = get_choices(map, (x, y), visited)
	x, y, path_lenght, current_choices, new_visited = follow_path(map, (x, y), current_choices)
	visited = *visited, *new_visited
	if (x, y) == to:
		return path_lenght
	options = []
	for dir_x, dir_y in current_choices:
		new_frm = (x + dir_x, y + dir_y)
		options.append(get_longest_path(map, new_frm, to, visited))
	possible_paths = [path for path in options if path != None]
	return None if len(possible_paths) == 0 else (max(possible_paths) + path_lenght + 1)
	
start = (input_lines[0].index('.'), 0)
end = (input_lines[-1].index('.'), len(input_lines) - 1)

print(get_longest_path(tuple(input_lines), start, end)) # part 1

def get_dirs(tile):
	return [(1, 0), (-1, 0), (0, 1), (0, -1)]

print(get_longest_path(tuple(input_lines), start, end)) # part 2


# def is_path(map, cell):
# 	x, y = cell
# 	if y < 0 or x < 0:
# 		return False
# 	if y >= len(map) or x >= len(map[y]):
# 		return False
# 	return map[y][x] != '#'

# def get_dirs(tile):
# 	return [(1, 0), (-1, 0), (0, 1), (0, -1)]

# def get_choices(map, cell, visited):
# 	x, y = cell
# 	if y < 0 or x < 0:
# 		return []
# 	if y >= len(map) or x >= len(map[y]):
# 		return []
# 	return tuple((dir_x, dir_y) for dir_x, dir_y in get_dirs(map[y][x]) if is_path(map, (x + dir_x, y + dir_y)) and not (x + dir_x, y + dir_y) in visited)

# def follow_path(map, frm, current_choices):
# 	x, y = frm
# 	path_lenght = 0
# 	visited = (x, y),
# 	while len(current_choices) == 1:
# 		dir_x, dir_y = current_choices[0]
# 		x, y = (x + dir_x, y + dir_y)
# 		visited = *visited, (x, y)
# 		path_lenght += 1
# 		current_choices = get_choices(map, (x, y), visited)
# 	return (x, y, path_lenght, current_choices)

# hallways = []
# x, y, path_lenght, current_choices = follow_path(input_lines, start, get_choices(input_lines, start, ()))
# hallways.append((start, (x, y), path_lenght))

# print(hallways)