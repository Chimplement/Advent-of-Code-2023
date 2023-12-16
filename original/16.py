with open("input.txt", "r") as input_file:
	input : str = input_file.read().split("\n")

LEFT = 0
RIGHT = 1
UP = 2
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

def new_beam_direction(current_dir : int, char : str) -> list[int]:
	if char == ".":
		return [current_dir]
	if char == "|":
		if (current_dir == LEFT or current_dir == RIGHT):
			return [UP, DOWN]
		return [current_dir]
	if char == "-":
		if (current_dir == UP or current_dir == DOWN):
			return [LEFT, RIGHT]
		return [current_dir]
	if char == "/":
		return [[DOWN, UP, RIGHT, LEFT][current_dir]]
	if char == "\\":
		return [[UP, DOWN, LEFT, RIGHT][current_dir]]
	return [current_dir]

def trace_beam(map : list[str], start : tuple[int, int], dir : int, energized_tiles : set[tuple[int, int, int]] = set()) -> set[tuple[int, int, int]]:
	beam_position = start
	while is_in_bounds(map, beam_position) and not (beam_position[0], beam_position[1], dir) in energized_tiles:
		energized_tiles.add((beam_position[0], beam_position[1], dir))
		new_dirs = new_beam_direction(dir, map[beam_position[1]][beam_position[0]])
		if len(new_dirs) > 1:
			for d in new_dirs:
				trace_beam(map, beam_position, d, energized_tiles)
			return energized_tiles
		dir = new_dirs[0]
		beam_position = (
			beam_position[0] + (-1 if dir == LEFT else 1 if dir == RIGHT else 0),
			beam_position[1] + (-1 if dir == UP else 1 if dir == DOWN else 0)
		)
	return energized_tiles

def remove_beam_directions(energized_tiles : set[tuple[int, int, int]]) -> set[tuple[int, int]]:
	tiles = set()
	for energized_tile in energized_tiles:
		tiles.add((energized_tile[0], energized_tile[1]))
	return tiles

print(len(remove_beam_directions(trace_beam(input, (0, 0), RIGHT))))

best_configuration = 0

for y in range(len(input)):
	best_configuration = max(len(remove_beam_directions(trace_beam(input, (0, y), RIGHT, set()))), best_configuration)
	best_configuration = max(len(remove_beam_directions(trace_beam(input, (len(input[0]) - 1, y), LEFT, set()))), best_configuration)

for x in range(len(input[0])):
	best_configuration = max(len(remove_beam_directions(trace_beam(input, (x, 0), DOWN, set()))), best_configuration)
	best_configuration = max(len(remove_beam_directions(trace_beam(input, (x, len(input) - 1), UP, set()))), best_configuration)

print(best_configuration)