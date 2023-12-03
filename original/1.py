input_string : str = """..."""

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

def get_first_digit(line : str) -> str:
	for i in range(len(line)):
		if line[i].isdigit():
			return line[i]
		for j in range(1, len(spelled_digits)):
			if line.startswith(spelled_digits[j], i):
				return str(j)
	return ("0")

def get_last_digit(line : str) -> str:
	for i in range(len(line) - 1, -1, -1):
		if line[i].isdigit():
			return line[i]
		for j in range(1, len(spelled_digits)):
			if line.endswith(spelled_digits[j], 0, i + 1):
				return str(j)
	return ("0")

cal_value = 0

for line in input_string.splitlines():
	cal_value += int(get_first_digit(line) + get_last_digit(line))

print(cal_value)