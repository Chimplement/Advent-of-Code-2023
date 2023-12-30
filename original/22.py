with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

# def parse_lines(input_lines : list[str]) -> list[list[list[int]]]:
# 	max_x = 0
# 	max_y = 0
# 	max_z = 0
# 	for line in input_lines:
# 		for coord in line.split("~"):
# 			x, y, z = coord.split(",")
# 			max_x = max(max_x, int(x))
# 			max_y = max(max_y, int(y))
# 			max_z = max(max_z, int(z))
# 	map = []
# 	for x in range(max_x + 1):
# 		map.append([])
# 		for y in range(max_y + 1):
# 			map[x].append([])
# 			for z in range(max_z +1):
# 				map[x][y].append(0)
# 	brick_number = 1
# 	for line in input_lines:
# 		start, end = line.split("~")
# 		start_x, start_y, start_z = start.split(",")
# 		start_x, start_y, start_z = int(start_x), int(start_y), int(start_z)
# 		end_x, end_y, end_z = end.split(",")
# 		end_x, end_y, end_z = int(end_x), int(end_y), int(end_z)
# 		for x in range(start_x, end_x + 1):
# 			for y in range(start_y, end_y + 1):
# 				for z in range(start_z, end_z + 1):
# 					map[x][y][z] = brick_number
# 		brick_number += 1
# 	return (map, brick_number - 1)

# def is_supported(map, brick_number):
# 	for x in range(len(map)):
# 		for y in range(len(map[x])):
# 			for z in range(len(map[x][y])):
# 				if map[x][y][z] == brick_number:
# 					if (z - 1 < 0):
# 						return True
# 					if map[x][y][z - 1] != 0 and map[x][y][z - 1] != brick_number:
# 						return True
# 	return False

# def drop_bricks(map, brick_count):
# 	has_fallen = True
# 	while has_fallen:
# 		has_fallen = False
# 		for i in range(1, brick_count + 1):
# 			if (is_supported(map, i)):
# 				continue
# 			for x in range(len(map)):
# 				for y in range(len(map[x])):
# 					for z in range(len(map[x][y])):
# 						if map[x][y][z] == i:
# 							if (z - 1 < 0):
# 								continue
# 							map[x][y][z - 1] = map[x][y][z]
# 							map[x][y][z] = 0
# 			has_fallen = True
		
# def is_save(map, brick_number):
# 	supported = set()
# 	not_supported = set()
# 	for x in range(len(map)):
# 		for y in range(len(map[x])):
# 			for z in range(len(map[x][y])):
# 				if map[x][y][z] == brick_number or map[x][y][z] == 0:
# 					continue
# 				if (z - 1 < 0):
# 					supported.add(map[x][y][z])
# 					continue
# 				if (map[x][y][z - 1] == brick_number or map[x][y][z - 1] == 0 or map[x][y][z - 1] == map[x][y][z]):
# 					not_supported.add(map[x][y][z])
# 				else:
# 					supported.add(map[x][y][z])
# 	return len(not_supported.difference(supported)) == 0

# map, brick_count = parse_lines(input_lines)
# drop_bricks(map, brick_count)
# part1 = 0
# for i in range(1, brick_count + 1):
# 	part1 += is_save(map, i)
# print(part1)

X = 0
Y = 1
Z = 2

def get_brick(bricks, x, y, z):
	for brick in bricks:
		start_x, start_y, start_z = brick[0]
		end_x, end_y, end_z = brick[1]
		if x >= start_x and x <= end_x:
			if y >= start_y and y <= end_y:
				if z >= start_z and z <= end_z:
					return (brick)
	return None

def is_supported(bricks, brick ,filter = None):
	start_x, start_y, start_z = brick[0]
	end_x, end_y, end_z = brick[1]
	if (start_z == 0 or end_z == 0):
		return True
	for x in range(start_x, end_x + 1):
		for y in range(start_y, end_y + 1):
			for z in range(start_z, end_z + 1):
				supporting_brick = get_brick(bricks, x, y, z - 1)
				if supporting_brick == None or supporting_brick == brick or supporting_brick == filter:
					continue
				return True
	return False

def is_supportedr(supports_list, brick, filter = []):
	has_support = False
	start_x, start_y, start_z = brick[0]
	end_x, end_y, end_z = brick[1]
	if (start_z == 0 or end_z == 0):
		return True
	for x in range(start_x, end_x + 1):
		for y in range(start_y, end_y + 1):
			for z in range(start_z, end_z + 1):
				supporting_brick = get_brick(bricks, x, y, z - 1)
				if supporting_brick == None or supporting_brick == brick or supporting_brick in filter:
					continue
				has_support |= is_supportedr(supports_list, supporting_brick, filter)
	return has_support


def get_supports(bricks, brick):
	start_x, start_y, start_z = brick[0]
	end_x, end_y, end_z = brick[1]
	if (start_z == 0 or end_z == 0):
		return []
	supports = []
	for x in range(start_x, end_x + 1):
		for y in range(start_y, end_y + 1):
			for z in range(start_z, end_z + 1):
				supporting_brick = get_brick(bricks, x, y, z - 1)
				if supporting_brick == None or supporting_brick == brick:
					continue
				if not supporting_brick in supports:
					supports.append(supporting_brick)
	return supports

def drop_bricks(bricks):
	updating = True
	while updating:
		updating = False
		for brick in bricks:
			while not is_supported(bricks, brick):
				brick[0][Z] -=1
				brick[1][Z] -= 1
				updating = True

def list_supports(bricks):
	supports_list = {}
	for brick in bricks:
		supports_list[brick] = get_supports(bricks, brick)
	return supports_list

bricks = [tuple([[int(n) for n in coord.split(",")] for coord in line.split("~")]) for line in input_lines]
drop_bricks(bricks)
bricks = [(tuple(brick[0]), tuple(brick[1])) for brick in bricks]
print("brick dropped")
supports_list = list_supports(bricks)
print("supports listed")
part1 = 0
for brick in bricks:
	is_save = True
	for supports in supports_list.values():
		if brick in supports and len(supports) == 1:
			is_save = False
			break
	part1 += is_save
print("part1:", part1)

part2 = 0
for brick in bricks:
	for brick2 in bricks:
		part2 += not is_supportedr(bricks, brick, [brick2])
	# chain_size = -1
	# this_chain = []
	# chain_members_queue = [brick]
	# while len(chain_members_queue) > 0:
	# 	current = chain_members_queue.pop(0)
	# 	if (current in this_chain):
	# 		continue
	# 	chain_size += 1
	# 	this_chain.append(current)
	# 	for b in supports_list[current]:
	# 		if not is_supportedr(bricks, b, this_chain):
	# 			chain_members_queue.append(b)
	# print(chain_size)
	# part2 += chain_size

print("part2:", part2)