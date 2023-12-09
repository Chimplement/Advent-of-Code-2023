with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

def get_differences(sequence : list[int]) -> list[int]:
	differences = []
	for i in range(1, len(sequence)):
		differences.append(sequence[i] - sequence[i - 1])
	return differences

def find_next_value(sequence : list[int]) -> int:
	if (any(sequence)):
		return (sequence[-1] + find_next_value(get_differences(sequence)))
	return 0

sequences : list[list[int]] = [[int(word) for word in line.split()] for line in input_lines]

print(sum(find_next_value(sequence) for sequence in sequences))
print(sum(find_next_value(sequence[::-1]) for sequence in sequences))