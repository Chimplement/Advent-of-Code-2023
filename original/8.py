from functools import lru_cache

with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

map = input_lines[2:]

@lru_cache(maxsize=None)
def find_node(node : str) -> str:
	for map_node in map:
		if map_node[:3].endswith(node):
			return (map_node)
	return ("")

def get_left_node(node : str) -> str:
	return node.split(" = ")[1].split(", ")[0].removeprefix("(")

def get_right_node(node : str) -> str:
	return node.split(" = ")[1].split(", ")[1].removesuffix("\n").removesuffix(")")

sequence = input_lines[0].removesuffix("\n")


current_node = find_node("AAA")
steps = 0
while (not current_node.startswith("ZZZ")):
	next_node : str
	if sequence[steps % len(sequence)] == 'L':
		next_node = get_left_node(current_node)
	elif sequence[steps % len(sequence)] == 'R':
		next_node = get_right_node(current_node)
	current_node = find_node(next_node)
	steps += 1

print(steps)

def get_nodes_ending_with(suffix : str) -> list[str]:
	nodes : list[str] = []
	for map_node in map:
		if map_node[:3].endswith(suffix):
			nodes.append(map_node)
	return (nodes)

current_nodes = get_nodes_ending_with("A")
original_nodes = current_nodes.copy()
steps_per_nodes = [-1] * len(original_nodes)
steps = 0
while (not all([count != -1 for count in steps_per_nodes])):
	for i, current_node in enumerate(current_nodes):
		if (steps_per_nodes[i] != -1):
			continue
		next_node : str
		if sequence[steps % len(sequence)] == 'L':
			next_node = get_left_node(current_node)
		elif sequence[steps % len(sequence)] == 'R':
			next_node = get_right_node(current_node)
		current_nodes[i] = find_node(next_node)
		if current_nodes[i][:3].endswith("Z"):
			steps_per_nodes[i] = steps + 1
	steps += 1

import math

def lcm_of_array(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = abs(result * num) // math.gcd(result, num)
    return result

print(lcm_of_array(steps_per_nodes))