import networkx as nx

with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

def parse_line(line) -> list:
	connections = []
	component_from, components_to = line.split(": ")
	for component in components_to.split(" "):
		connections.append((component_from, component))
	return (connections)

connections = sum([parse_line(line) for line in input_lines], [])

graph = nx.Graph(connections)
graph.remove_edges_from(nx.minimum_edge_cut(graph))
groups = list(nx.connected_components(graph))
print(len(groups[0]) * len(groups[1]))