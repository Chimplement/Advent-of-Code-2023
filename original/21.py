with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

def get_map_tile(map : list[str], x, y):
	if y < 0 or x < 0:
		return ('.')
	if y >= len(map) or x >= len(map[y]):
		return ('.')
	return map[y][x]
def iterate(map : list[str]):
	new_map : list[str] = []
	for y,row in enumerate(map):
		new_map.append("")
		for x,c in enumerate(row):
			if (get_map_tile(map, x, y) == 'O'):
				new_map[y] += '.'
			elif (get_map_tile(map, x, y) == '.'):
				if (get_map_tile(map, x + 1, y) == 'O' or get_map_tile(map, x - 1, y) == 'O' or get_map_tile(map, x, y + 1) == 'O' or get_map_tile(map, x, y - 1) == 'O'):
					new_map[y] += 'O'
				else:
					new_map[y] += '.'
			else:
				new_map[y] += c
	return new_map

def fill_from(map : list[str], start_x, start_y, times):
	map = map.copy()
	map[start_y] = map[start_y][:start_x] + 'O' + map[start_y][start_x+1:]
	for _ in range(times):
		map = iterate(map)
	return map

start_x, start_y = sum([[(x,y) for x,c in enumerate(line) if c == 'S'] for y,line in enumerate(input_lines) if 'S' in line],[])[0]

map = [line.replace('S', '.') for line in input_lines]


part1 = 0
for row in fill_from(map, start_x, start_y, 64):
	part1 += row.count('O')
print(part1)

def map_loop(map : list[str], times):
	new_map : list[str] = []
	for loop_y in range(times):
		for y,row in enumerate(map):
			new_map.append("")
			for _ in range(times):
				for x,c in enumerate(row):
					new_map[y + len(map) * loop_y] += c
	return new_map


from math import *

looped_map = map_loop(map, 5)

steps = 26501365
height = len(map)
widht = len(map[0])

size = widht = height

plots = [0, 0, 0]
for row in fill_from(looped_map, start_x + size * 2, start_y + size * 2, size//2):
	plots[0] += row.count('O')

for row in fill_from(looped_map, start_x + size * 2, start_y + size * 2, size//2 + size):
	plots[1] += row.count('O')

for row in fill_from(looped_map, start_x + size * 2, start_y + size * 2, size//2 + size * 2):
	plots[2] += row.count('O')

b0 = plots[0]
b1 = plots[1]-plots[0]
b2 = plots[2]-plots[1]

n = steps//size
part2 = b0 + b1*n + (n*(n-1)//2)*(b2-b1) # find nth itheration of the first the plots
print(part2)


