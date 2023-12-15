with open("input.txt", "r") as input_file:
	input : str = input_file.read()

def hash(s : str) -> int:
	current_value = 0
	for c in s:
		current_value += ord(c)
		current_value *= 17
		current_value %= 256
	return (current_value)

def do_action(boxes : list[list[list[str, int]]], string : str) -> None:
	label = string.split("=")[0].split("-")[0]
	box = hash(label)
	for i,lens in enumerate(boxes[box]):
		if lens[0] == label:
			if "-" in string: 
				del boxes[box][i]
				return
			if "=" in string:
				boxes[box][i] = [label, int(string[string.index("=")+1:])]
				return
	if "=" in string:
		boxes[box].append([label, int(string[string.index("=")+1:])]) 

print("step 1:", sum(hash(step) for step in input.split(",")))

boxes = [[] for _ in range(256)]

for step in input.split(","):
	do_action(boxes, step)

focussing_power = 0

for i,box in enumerate(boxes):
	for j,lens in enumerate(box):
		focussing_power += (i+1)*(j+1)*lens[1]

print("step 2:", focussing_power)