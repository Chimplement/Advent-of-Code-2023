with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

def get_differences(s1 : str, s2 : str) -> int:
	differences = 0
	for i, c in enumerate(s1):
		if c != s2[i]:
			differences += 1
	return (differences)

def	is_mirror(part1 : list[str], part2 : list[str]) -> bool:
	part1.reverse()
	differences = 0
	for i, line in enumerate(part1):
		if i >= len(part2):
			break
		if line != part2[i]:
			if get_differences(line, part2[i]) == 1:
				differences += 1
				if differences > 1:
					return False
			else:
				return False
	return differences == 1

def find_vertical_mirror(map : list[str]) -> int:
	for i in range(1, len(map)):
		if is_mirror(map[:i], map[i:]):
			return i
	return -1

def find_horizontal_mirror(map : list[str]) -> int:
	rotated_map = ["".join(line) for line in zip(*map)]
	return find_vertical_mirror(rotated_map)

def find_mirror(map : list[str]) -> int:
	mirror = -1
	mirror = find_vertical_mirror(map)
	if mirror != -1:
		return (mirror * 100)
	mirror = find_horizontal_mirror(map)
	if mirror != -1:
		return (mirror)
	return (-1)

maps = []
current_map = []
for line in input_lines:
	if line == "":
		maps.append(current_map)
		current_map = []
		continue
	current_map.append(line)
maps.append(current_map)

print(sum([find_mirror(map) for map in maps]), sep="\n")