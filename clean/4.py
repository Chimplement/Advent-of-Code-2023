with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

def get_winning_numbers(line : str) -> list[int]:
	your_winning_numbers = []
	line = line.removesuffix("\n")
	numbers_str = line.split(": ")[1]
	winning_number_str = numbers_str.split(" | ")[0]
	your_number_str = numbers_str.split(" | ")[1]
	winning_numbers = []
	for number_str in winning_number_str.split(" "):
		if len(number_str) > 0:
			winning_numbers.append(int(number_str))
	your_numbers = []
	for number_str in your_number_str.split(" "):
		if len(number_str) > 0:
			your_numbers.append(int(number_str))
	for number in your_numbers:
		if number in winning_numbers:
			your_winning_numbers.append(number)
	your_numbers
	return (your_winning_numbers)

def get_card_worths(lines : list[str]) -> list[int]:
	worths = []
	for line in lines:
		winning_numbers = get_winning_numbers(line)
		if len(winning_numbers) > 0:
			worths.append(1 * pow(2, len(winning_numbers) - 1))
		else:
			worths.append(0)
	return worths

def get_copies(lines : list[str]) -> list[int]:
	copies = [1] * len(lines)
	for line_n, line in enumerate(lines):
		winning_numbers = get_winning_numbers(line)
		for i in range(line_n + 1, line_n + 1 + len(winning_numbers)):
			if (i < len(lines)):
				copies[i] += copies[line_n]
	return copies

print("part1:", sum(get_card_worths(input_lines)))
print("part2:", sum(get_copies(input_lines)))