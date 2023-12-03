with open("input.txt", "r") as input_file:
	input_lines : str = input_file.readlines()

def parse_input(input_lines : list[str]) -> list[dict[str, int]]:
	parsed_input = []
	for i, line in enumerate(input_lines):
		parsed_line = {}
		parsed_line["ID"] = i + 1
		subsets = line.split(": ")[1].split("; ")
		parsed_line["red"] = 0
		parsed_line["green"] = 0
		parsed_line["blue"] = 0
		for subset in subsets:
			for cubes_of_color in subset.split(", "):
				cubes = cubes_of_color.split(" ")[0]
				color = cubes_of_color.split(" ")[1]
				color = color.removesuffix('\n');
				if (color in ["red", "green", "blue"]):
					parsed_line[color] = max(parsed_line[color], int(cubes))
		parsed_input.append(parsed_line)
	return parsed_input

def possible_games(games : list[dict[str, int]], red_cubes : int, green_cubes : int, blue_cubes : int) -> list[int]:
	possible = []
	for game in games:
		if game["red"] <= red_cubes:
			if game["green"] <= green_cubes:
				if game["blue"] <= blue_cubes:
					possible.append(game["ID"])
	return possible

def game_powers(game : list[dict[str, int]]) -> list[int]:
	powers = []
	for game in games:
		powers.append(game["red"] * game["green"] * game["blue"])
	return (powers)

games = parse_input(input_lines)
print(sum(possible_games(games, 12, 13, 14)))
print(sum(game_powers(games)))
