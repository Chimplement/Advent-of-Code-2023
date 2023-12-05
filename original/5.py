with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()


def convert_seed_with_range(range_info : tuple[int, int, int], seed : int) -> int:
	if seed >= range_info[1] and seed < range_info[1] + range_info[2]:
		return range_info[0] + seed - range_info[1]
	return -1

def convert_map(map : list[str], seeds) -> list[int]:
	converted_seeds  : list[int] = [-1] * len(seeds)
	i = 0
	map_range_info : list[list[int]] = [[int(number_str) for number_str in line.removesuffix("\n").split(" ")] for line in map]
	while i < len(seeds):
		seed = seeds[i]
		found = False
		for range_info in map_range_info:
			value = convert_seed_with_range(range_info, seed)
			if value != -1:
				converted_seeds[i] = value
				found = True
				break
		if (not found):
			converted_seeds[i] = seed
		i += 1
	return converted_seeds

seeds : list[int] = [int(number_str) for number_str in input_lines[0].removesuffix("\n").split(": ")[1].split(" ")]

original_seeds = seeds.copy()

last_newline = input_lines.index("\n")
while True:
	if "\n" in input_lines[last_newline + 1:]:
		next_newline = last_newline + 1 + input_lines[last_newline + 1:].index("\n")
		seeds = convert_map(input_lines[last_newline + 2:next_newline], seeds)
		last_newline = next_newline
	else:
		seeds = convert_map(input_lines[last_newline + 2:], seeds)
		break

print(min(seeds))

# part 2

def convert_seed_ranges(range_info : tuple[int, int, int], seed_range : tuple[int, int]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
	if (seed_range[0] < range_info[1] and seed_range[1] < range_info[1]):
		return ([], [seed_range])
	if (seed_range[0] >= range_info[1] + range_info[2] and seed_range[1] > range_info[1] + range_info[2]):
		return ([], [seed_range])
	if (seed_range[0] >= range_info[1] and seed_range[1] <= range_info[1] + range_info[2]):
		return ([(range_info[0] + seed_range[0] - range_info[1], range_info[0] + seed_range[1] - range_info[1])], [])
	if (seed_range[0] < range_info[1] and seed_range[1] > range_info[1] + range_info[2]):
		return (
			[
				(range_info[0], range_info[0] + range_info[2])
			], 
			[
				(seed_range[0], range_info[1]),
				(range_info[1] + range_info[2], seed_range[1])
			]
		)
	if (seed_range[0] < range_info[1] and seed_range[1] <= range_info[1] + range_info[2]):
		return (
			[
				(range_info[0], range_info[0] + seed_range[1] - range_info[1])
			], 
			[
				(seed_range[0], range_info[1])
			]
		)
	if (seed_range[0] >= range_info[1] and seed_range[1] >= range_info[1] + range_info[2]):
		return (
			[
				(range_info[0] + seed_range[0] - range_info[1], range_info[0] + range_info[2])
			], 
			[
				(range_info[1] + range_info[2], seed_range[1])
			]
		)
	return ([], [seed_range])


def convert_map_seed_ranges(map : list[str], seed_ranges : list[tuple[int, int]]) -> list[tuple[int, int]]:
	converted_seed_ranges  : list[int] = []
	left_to_convert : list[tuple[int, int]] = seed_ranges.copy()
	map_range_info : list[tuple[int, int, int]] = [[int(number_str) for number_str in line.removesuffix("\n").split(" ")] for line in map]
	for range_info in map_range_info:
		new_left_to_convert : list[tuple[int, int]] = []
		for seed_range in left_to_convert:
			inside_ranges, outside_ranges = convert_seed_ranges(range_info, seed_range)
			new_left_to_convert.extend(outside_ranges)
			converted_seed_ranges.extend(inside_ranges)
		left_to_convert = new_left_to_convert
	converted_seed_ranges.extend(left_to_convert)
	return converted_seed_ranges

seed_ranges : list[tuple[int, int]] = []
i = 0
while i < len(original_seeds):
	seed_ranges.append((original_seeds[i], original_seeds[i] + original_seeds[i + 1]))
	i += 2

last_newline = input_lines.index("\n")
while True:
	if "\n" in input_lines[last_newline + 1:]:
		next_newline = last_newline + 1 + input_lines[last_newline + 1:].index("\n")
		seed_ranges = convert_map_seed_ranges(input_lines[last_newline + 2:next_newline], seed_ranges)
		last_newline = next_newline
	else:
		seeds = convert_map_seed_ranges(input_lines[last_newline + 2:], seed_ranges)
		break


print(min(seed_ranges, key = lambda seed_range: seed_range[0])[0])