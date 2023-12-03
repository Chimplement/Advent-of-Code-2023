
input_lines : list[str] = open("input").readlines()

def is_char_adjacent(line_n : int, i : int, lines : list[str]) -> bool:
	for x in range(-1, 2):
		for y in range(-1, 2):
			if (line_n + y) < 0 or (line_n + y) >= len(lines):
				continue
			if (i + x) < 0 or (i + x) >= len(lines[line_n + y]):
				continue
			if lines[line_n + y][i + x] != '.' and not lines[line_n + y][i + x].isdigit() and lines[line_n + y][i + x] != '\n':
				return (True)
	return (False)

def is_number_adjacent(line_n : int, i : int, lines : list[str]) -> bool:
	while (lines[line_n][i].isdigit()):
		if is_char_adjacent(line_n, i, lines):
			return True
		i += 1
	return False

def number_len(line_n : int, i : int, lines : list[str]) -> int:
	length = 0
	while (lines[line_n][i + length].isdigit()):
		length += 1
	return length

def get_adjacent_numbers_to_symbol(lines : list[str]) -> list[int]:
	last_was_digit = False
	numbers = []
	for line_n, line in enumerate(lines):
		for i, char in enumerate(line):
			if (char.isdigit() and not last_was_digit):
				if is_number_adjacent(line_n, i, lines):
					numbers.append(int(line[i:i + number_len(line_n, i, lines)]))
			last_was_digit = char.isdigit()
	return (numbers)

def get_number(line_n : int, i : int, lines : list[str]) -> tuple[int]:
	if (not lines[line_n][i].isdigit()):
			return (0)
	while (lines[line_n][i].isdigit()):
		i -= 1
	i += 1
	return (i, int(lines[line_n][i:i + number_len(line_n, i, lines)]))

def get_gear_adjacent_numbers(line_n : int, i : int, lines : list[str]) -> list[int]:
	numbers = []
	number_starts = []
	for x in range(-1, 2):
		for y in range(-1, 2):
			if (line_n + y) < 0 or (line_n + y) >= len(lines):
				continue
			if (i + x) < 0 or (i + x) >= len(lines[line_n + y]):
				continue
			if lines[line_n + y][i + x].isdigit():
				number_start, number = get_number(line_n + y, i + x, lines)
				if (not (number_start, line_n + y) in number_starts):
					number_starts.append((number_start, line_n + y))
					numbers.append(number)
	return numbers

def get_gear_ratios(lines : list[str]) -> list[int]:
	ratios = []

	for line_n, line in enumerate(lines):
		for i, char in enumerate(line):
			if char == '*':
				numbers = get_gear_adjacent_numbers(line_n, i, lines)
				if len(numbers) == 2:
					ratios.append(numbers[0] * numbers[1])

	return ratios

print(sum(get_adjacent_numbers_to_symbol(input_lines)))
print(sum(get_gear_ratios(input_lines)))