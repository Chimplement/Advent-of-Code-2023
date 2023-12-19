with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

workflow = input_lines[:input_lines.index("")]
parts = input_lines[input_lines.index("") + 1:]

workflow = {line[:line.index('{')]:tuple(line[line.index('{'):].removeprefix('{').removesuffix('}').split(',')) for line in workflow}
parts = [{line.split('=')[0]:int(line.split('=')[1]) for line in line.removeprefix('{').removesuffix('}').split(',')} for line in parts]

def is_accepted(part, workflow):
	current_rule = "in"
	while current_rule:
		for step in workflow[current_rule]:
			if ":" in step:
				goal = step.split(':')[1]
				if '<' in step:
					param = step.split('<')[0]
					value = int(step.split(':')[0].split('<')[1])
					if part[param] < value:
						current_rule = goal
						break
				elif '>' in step:
					param = step.split('>')[0]
					value = int(step.split(':')[0].split('>')[1])
					if part[param] > value:
						current_rule = goal
						break
			else:
				current_rule = step
				break
		if (current_rule == "A"):
			return True
		elif (current_rule == "R"):
			return False
	return False


sum_accepted = 0
for part in parts:
	if is_accepted(part, workflow):
		sum_accepted += sum(part.values())

print(sum_accepted)

def devide_range(ranges, param, value, op):
	passed = ranges.copy()
	failed = ranges.copy()
	if op == '<':
		if ranges[param][1] < value:
			return passed, []
		if ranges[param][0] < value:
			passed[param] = (ranges[param][0], value - 1)
			failed[param] = (value, ranges[param][1])
			return passed, failed
		return [], failed
	if op == '>':
		if ranges[param][0] > value:
			return passed, []
		if ranges[param][1] > value:
			passed[param] = (value + 1, ranges[param][1])
			failed[param] = (ranges[param][0], value)
			return passed, failed
		return [], failed
	return [], []


def get_accepted_values(workflow, ranges=None, current_rule = "in", rule_step = 0):
	if ranges == None:
		ranges = {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}
	if ranges == []:
		return []
	current_step = rule_step
	while current_rule:
		if (current_rule == "A"):
			return [ranges]
		elif (current_rule == "R"):
			return []
		for step in workflow[current_rule][current_step:]:
			current_step += 1
			if ":" in step:
				goal = step.split(':')[1]
				if '<' in step:
					rule_param = step.split('<')[0]
					rule_value = int(step.split(':')[0].split('<')[1])
					passed, failed = devide_range(ranges, rule_param, rule_value, '<')
					return get_accepted_values(workflow, passed, goal, 0) + get_accepted_values(workflow, failed, current_rule, current_step)
				elif '>' in step:
					rule_param = step.split('>')[0]
					rule_value = int(step.split(':')[0].split('>')[1])
					passed, failed = devide_range(ranges, rule_param, rule_value, '>')
					return get_accepted_values(workflow, passed, goal, 0) + get_accepted_values(workflow, failed, current_rule, current_step)
			else:
				current_rule = step
				break
		current_step = 0
	return False

accepted = 0

for range in get_accepted_values(workflow):
	range_combinations = 1
	for c in 'x', 'm', 'a', 's':
		lenght = range[c][1] - range[c][0] + 1
		range_combinations *= lenght
	accepted += range_combinations


print(accepted)