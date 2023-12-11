with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

EXPANSION = 1000000

expanded_rows = []
expanded_columns = []

universe = []
for i, line in enumerate(input_lines):
	line = line.removesuffix("\n")
	if (line.count("#") == 0):
		expanded_rows.append(i)
	universe.append(line)

for i, char in enumerate(input_lines[0]):
	if (char == "."):
		if (not any(True for line in input_lines if line[i] == "#")):
			expanded_columns.append(i)

universe_positions = []

y_offset = 0
for y, row in enumerate(universe):
	if y in expanded_rows:
		y_offset += EXPANSION - 1
	x_offset = 0
	for x, char in enumerate(row):
		if x in expanded_columns:
			x_offset += EXPANSION - 1
		if char == "#":
			universe_positions.append((x_offset + x, y_offset + y))

distances = []

for position1 in universe_positions:
	for position2 in universe_positions:
		if position1 == position2:
			continue
		distances.append(abs(position2[0] - position1[0]) + abs(position2[1] - position1[1]))

print("part2: ", sum(distances) // 2)