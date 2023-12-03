with open("input.txt", "r") as input_file:
	input_lines : str = input_file.readlines()

spelled_digits : [str] = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine"
]

def get_first_digit(line : str) -> int:
	for i in range(len(line)):
		if line[i].isdigit():
			return int(line[i])
		for j in range(1, len(spelled_digits)):
			if line.startswith(spelled_digits[j], i):
				return int(j)
	return 0

def get_last_digit(line : str) -> int:
	for i in range(len(line) - 1, -1, -1):
		if line[i].isdigit():
			return int(line[i])
		for j in range(1, len(spelled_digits)):
			if line.endswith(spelled_digits[j], 0, i + 1):
				return int(j)
	return 0

sum = 0
for line in input_lines:
	sum += get_first_digit(line) * 10 + get_last_digit(line)
print(sum)