with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

map = [line.removesuffix("\n") for line in input_lines]

def find_start(map : list[str]) -> tuple[int, int]:
	for y, row in enumerate(map):
		for x, char in enumerate(row):
			if char == 'S':
				return (x, y)
	return (0, 0)

def get_connecting_pipes(map : list[str], start : tuple[int, int]) -> list[tuple[int, int]]:
	if map[start[1]][start[0]] == 'S':
		connecting_pipes = []
		for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			if start in get_connecting_pipes(map, (start[0] + offset[0], start[1] + offset[1])):
				connecting_pipes.append((start[0] + offset[0], start[1] + offset[1]))
		return (connecting_pipes)
	if map[start[1]][start[0]] == '|':
		return [(start[0], start[1] - 1), (start[0], start[1] + 1)]
	if map[start[1]][start[0]] == '-':
		return [(start[0] - 1, start[1]), (start[0] + 1, start[1])]
	if map[start[1]][start[0]] == 'L':
		return [(start[0], start[1] - 1), (start[0] + 1, start[1])]
	if map[start[1]][start[0]] == 'J':
		return [(start[0], start[1] - 1), (start[0] - 1, start[1])]
	if map[start[1]][start[0]] == '7':
		return [(start[0], start[1] + 1), (start[0] - 1, start[1])]
	if map[start[1]][start[0]] == 'F':
		return [(start[0], start[1] + 1), (start[0] + 1, start[1])]
	return [(0, 0), (0, 0)]

def flood_fill_pipe(map : list[str], start : tuple[int, int]) -> list[list[int]]:
	filled_map = [[-1 for char in row] for row in map]
	filled_map[start[1]][start[0]] = 0
	filled_last_iteration = True
	while filled_last_iteration:
		filled_last_iteration = False
		for y, row in enumerate(map):
			for x, char in enumerate(row):
				if (filled_map[y][x] == -1):
					continue
				for pipe in get_connecting_pipes(map, (x, y)):
					if (filled_map[pipe[1]][pipe[0]] == -1):
						filled_map[pipe[1]][pipe[0]] = filled_map[y][x] + 1
						filled_last_iteration = True
	return filled_map

start = find_start(map)
filled_pipes = flood_fill_pipe(map, start)

furthest_value = 0
furthest_position = start
for y, row in enumerate(filled_pipes):
	for x, value, in enumerate(row):
		if value > furthest_value:
			furthest_position = (x, y)
			furthest_value = value

print(furthest_value)

def is_in_loop(flood_filled_map : list[list[int]], tile : tuple[int, int]) -> list[tuple[int, int]]:
	if flood_filled_map[tile[1]][tile[0]] != -1:
		return []
	if (tile[0] < 1 or tile[0] >= len(flood_filled_map[0]) - 1 or tile[1] < 1 or tile[1] >= len(flood_filled_map) - 1):
		return []
	checked = [[False for char in row] for row in flood_filled_map]
	checked[tile[1]][tile[0]] = True
	filled_last_iteration = True
	tiles = []
	while filled_last_iteration:
		filled_last_iteration = False
		for y, row in enumerate(flood_filled_map):
			for x, value in enumerate(row):
				if (checked[y][x]):
					if (x < 1 or x >= len(row) - 1 or y < 1 or y >= len(flood_filled_map) - 1):
						return []
					continue
				if (value != -1):
					continue
				for offset in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, 1), (1, -1)]:
					if (x + offset[0] < 0 or x + offset[0] >= len(row) or y + offset[1] < 0 or y + offset[1] >= len(flood_filled_map)):
						continue
					if (checked[y + offset[1]][x + offset[0]]):
						checked[y][x] = True
						filled_last_iteration = True
						tiles.append((x, y))
	return tiles

def scale_map(map : list[str], flood_filled_map : list[list[int]]) -> list[list[int]]:
	new_map = [[-1 for x in range(len(flood_filled_map[y//2]) * 2)] for y in range(len(flood_filled_map) * 2)]
	for y, row in enumerate(flood_filled_map):
		for x, value in enumerate(row):
			new_map[y*2][x*2] = value
			conections = get_connecting_pipes(map, (x, y))
			if ((x + 1, y) in conections):
				new_map[y*2][x*2 + 1] = value
			if ((x, y + 1) in conections):
				new_map[y*2 + 1][x*2] = value
	return new_map

def find_inner_tiles(map : list[str], flood_filled_map : list[list[int]]) -> list[tuple[int, int]]:
	inner_tiles = []
	scaled_flood_filled_map = scale_map(map, flood_filled_map)
	for y, row in enumerate(flood_filled_map):
		for x, value in enumerate(row): 
			if (value != -1):
				continue
			if flood_filled_map[y][x] == -1:
				for tiles in is_in_loop(scaled_flood_filled_map, (x*2, y*2)):
					if (tiles[0] % 2 == 0 and tiles[1] % 2 == 0):
						if not (tiles[0]//2, tiles[1]//2) in inner_tiles:
							inner_tiles.append((tiles[0]//2, tiles[1]//2))
		# print("checked row", y)
	return (inner_tiles)

inner_tiles = find_inner_tiles(map, filled_pipes)
for y, row in enumerate(map):
	for x, char, in enumerate(row):
		if (x, y) in inner_tiles:
			print("I", end="")
		elif filled_pipes[y][x] != -1:
			print("#", end="")
		else:
			print(char, end="")
	print("")
print(len(inner_tiles))