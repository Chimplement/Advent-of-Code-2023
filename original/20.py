with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

LOW = 0
HIGH = 1

OFF = 0
ON = 1

modules = {}

signal_queue = []
total_high = 0
total_low = 0

def queue_all_destinations(frm, destinations, signal):
	global total_low, total_high
	for destination in destinations:
		if signal == LOW:
			total_low += 1
		elif signal == HIGH:
			total_high += 1
		signal_queue.append((frm, destination, signal))

def resolve_queue():
	while signal_queue != []:
		frm, destination, signal = signal_queue.pop(0)
		if destination in modules:
			modules[destination].recieve_signal(frm, signal)

class Module:
	def __init__(self, name, destinations):
		self.name = name
		self.destinations = destinations
		self.inputs = {}
	def add_input(self, frm):
		self.inputs[frm] = LOW
	def recieve_signal(self, frm : str, signal : int):
		self.inputs[frm] = signal
	def __str__(self) -> str:
		return self.name + " -> " + ", ".join(self.destinations)

class Broadcaster(Module):
	def recieve_signal(self, frm : str, signal : int):
		super().recieve_signal(frm, signal)
		queue_all_destinations(self.name, self.destinations, signal)

class FlipFlop(Module):
	def __init__(self, name, destinations):
		super().__init__(name, destinations)
		self.state = OFF
	def recieve_signal(self, frm : str, signal : int):
		super().recieve_signal(frm, signal)
		if signal == HIGH:
			return
		if signal == LOW:
			if self.state == OFF:
				self.state = ON
				queue_all_destinations(self.name, self.destinations, HIGH)
			elif self.state == ON:
				self.state = OFF
				queue_all_destinations(self.name, self.destinations, LOW)

class Conjunction(Module):
	def recieve_signal(self, frm : str, signal : int):
		super().recieve_signal(frm, signal)
		if any([input_signal == LOW for input_signal in self.inputs.values()]):
			queue_all_destinations(self.name, self.destinations, HIGH)
		else:
			queue_all_destinations(self.name, self.destinations, LOW)

type_map = {'%': FlipFlop, '&': Conjunction}

for line in input_lines:
	module, destinations = line.split(" -> ")
	destinations = destinations.split(", ")
	module_type : Module
	if module == "broadcaster":
		module_name = module
		module_type = Broadcaster
	else:
		module_name = module[1:]
		module_type = type_map[module[0]]
	modules[module_name] = module_type(module_name, destinations)

for module_name in modules:
	module = modules[module_name]
	for destination in module.destinations:
		if destination in modules:
			modules[destination].add_input(module_name)

# for i in range(1000):
# 	queue_all_destinations("button", ["broadcaster"], LOW)
# 	resolve_queue()

# print(total_high * total_low)

import math

dg_inputs = {input:-1 for input in modules["dg"].inputs}

button_presses = 0
found = False
while any([value == -1 for value in dg_inputs.values()]):
	button_presses += 1
	queue_all_destinations("button", ["broadcaster"], LOW)
	resolve_queue()
	for input in modules["dg"].inputs:
		if dg_inputs[input] == -1:
			if modules["dg"].inputs[input] == HIGH:
				dg_inputs[input] = button_presses
				print(modules["dg"].inputs)

print(math.lcm(*dg_inputs.values()))