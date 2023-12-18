with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

# dig_plan = [(line.split()[0], int(line.split()[1]), line.split()[2][1:-1]) for line in input_lines]
dig_plan = [(['R', 'D', 'L', 'U'][int(line.split()[2][-2])], int(line.split()[2][2:-2], 16)) for line in input_lines]

def create_trench(dig_plan) -> set:
	trench = set()
	current_pos = (0, 0)
	trench.add(current_pos)
	for instruction in dig_plan:
		for i in range(instruction[1]):
			current_pos = (
				current_pos[0] + (1 if instruction[0] == 'R' else -1 if instruction[0] == 'L' else 0),
				current_pos[1] + (1 if instruction[0] == 'D' else -1 if instruction[0] == 'U' else 0)
			)
			trench.add(current_pos)
	return trench

def fill_trench(trench : set) -> set:
	filled_trench = trench.copy()
	seen = set()
	top_left = [0, 0]
	botom_right = [0, 0]
	for tile in trench:
		if tile[0] < top_left[0]:
			top_left[0] = tile[0]
		if tile[1] < top_left[1]:
			top_left[1] = tile[1]
		if tile[0] > botom_right[0]:
			botom_right[0] = tile[0]
		if tile[1] > botom_right[1]:
			botom_right[1] = tile[1]
	for x in range(top_left[0], botom_right[0] + 1):
		for y in range(top_left[1], botom_right[1] + 1):
			if ((x, y) in trench):
				continue
			if ((x, y) in seen):
				continue
			current_check = set()
			current_check.add((x, y))
			new_added = True
			hit_edge = False
			while new_added:
				new_added = False
				for x2 in range(top_left[0], botom_right[0] + 1):
					for y2 in range(top_left[1], botom_right[1] + 1):
						if ((x2, y2) in trench):
							continue
						if (x2, y2) in seen:
							continue
						if (x2, y2) in current_check:
							continue
						if (set(((x2, y2 + 1), (x2, y2 - 1), (x2 + 1, y2), (x2 - 1, y2))) & current_check):
							current_check.add((x2, y2))
							new_added = True
							if (x2 >= botom_right[0] or x2 - 1 < top_left[0]):
								hit_edge = True
							if (y2 >= botom_right[1] or y2 - 1 < top_left[1]):
								hit_edge = True
			if not hit_edge:
				filled_trench.update(current_check)
			seen.update(current_check)

	# for y in range(top_left[1], botom_right[1] + 1):
	# 	for x in range(top_left[0], botom_right[0] + 1):
	# 		if ((x, y) in filled_trench):
	# 			print('#',end='')
	# 			continue
	# 		print('.',end='')
	# 	print('\n',end='')
		
	return filled_trench

def shoelace_trench(dig_plan) -> int:
	verticies = []
	current_pos = (0, 0)
	verticies.append(current_pos)
	for instruction in dig_plan:
		current_pos = (
			current_pos[0] + instruction[1] * (1 if instruction[0] == 'R' else -1 if instruction[0] == 'L' else 0),
			current_pos[1] + instruction[1] * (1 if instruction[0] == 'D' else -1 if instruction[0] == 'U' else 0)
		)
		verticies.append(current_pos)
	area2 = 0
	x = 1
	y = 1
	for instruction in dig_plan:
		nx = x + instruction[1] * (1 if instruction[0] == 'R' else -1 if instruction[0] == 'L' else 0)
		ny = y + instruction[1] * (1 if instruction[0] == 'D' else -1 if instruction[0] == 'U' else 0)
		area2 += x * ny
		area2 -= y * nx
		area2 += abs(nx - x)
		area2 += abs(ny - y)
		x = nx
		y = ny
	return area2 // 2 + 1
	
		


print(shoelace_trench(dig_plan))