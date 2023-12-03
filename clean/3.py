with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

def number_len(line_n : int, i : int, lines : list[str]) -> int:
	length = 0
	while (lines[line_n][i + length].isdigit()):
		length += 1
	return length

def get_number(line_n : int, i : int, lines : list[str]) -> tuple[tuple[int, int], int]:
	if (not lines[line_n][i].isdigit()):
			return 0
	while (lines[line_n][i].isdigit()):
		i -= 1
	i += 1
	return ((line_n, i), int(lines[line_n][i:i + number_len(line_n, i, lines)]))

def get_adjacent_numbers(line_n : int, i : int, lines : list[str]) -> tuple[list[tuple[int, int]], list[int]]:
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
				if not number_start in number_starts:
					numbers.append(number)
					number_starts.append(number_start)
	return (number_starts, numbers)

def get_numbers_adjacent_to_a_symbol(lines : list[str]) -> list[int]:
	numbers_adjacent_to_symbol = []
	number_starts = []
	for line_n, line in enumerate(lines):
		for i, char in enumerate(line):
			if char != '.' and char != '\n' and not char.isdigit():
				adjacent_number_starts, adjacent_numbers = get_adjacent_numbers(line_n, i, lines)
				for j in range(len(adjacent_numbers)):
					if not adjacent_number_starts[j] in number_starts:
						numbers_adjacent_to_symbol.append(adjacent_numbers[j])
						number_starts.append(adjacent_number_starts[j])
	return numbers_adjacent_to_symbol

def get_gear_ratios(lines : list[str]) -> list[int]:
	gear_ratios = []
	for line_n, line in enumerate(lines):
		for i, char in enumerate(line):
			if char == '*':
				_, numbers = get_adjacent_numbers(line_n, i, lines)
				if len(numbers) == 2:
					gear_ratios.append(numbers[0] * numbers[1])
	return gear_ratios

print(sum(get_numbers_adjacent_to_a_symbol(input_lines)))
print(sum(get_gear_ratios(input_lines)))