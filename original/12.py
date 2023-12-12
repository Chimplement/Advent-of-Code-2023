with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

records = [("?".join([line.split(" ")[0]]*5), tuple([int(s) for s in line.split(" ")[1].split(",")]*5)) for line in input_lines]

import functools
@functools.lru_cache(maxsize=None)
def get_arrangements(record : tuple[str, tuple[int, ...]], current_count = 0) ->list[str]:
	if record[0] == '':
		if len(record[1]) == 0:
			return 1
		if current_count == record[1][0] and len(record[1]) == 1:
			return 1
		return 0
	if len(record[1]) == 0 and record[0].count("#") > 0:
		return 0
	if record[0][0] == ".":
		if current_count > 0:
			if current_count != record[1][0]:
				return (0)
			return get_arrangements((record[0][1:], record[1][1:]), 0)
		return get_arrangements((record[0][1:], record[1]), 0)
	if record[0][0] == "#":
		current_count += 1
		if current_count > record[1][0]:
			return 0
		return get_arrangements((record[0][1:], record[1]), current_count)
	if record[0][0] == "?":
		total = 0
		total += get_arrangements(("."+record[0][1:], record[1]), current_count)
		total += get_arrangements(("#"+record[0][1:], record[1]), current_count)
		return total 
	return 0

	

total_arrangements = 0
for record in records:
	count = get_arrangements(record)
	print(count)
	total_arrangements += count

print("total:", total_arrangements)