input_text = """..."""

def parse_input(string : str) -> list:
	parsed_input = []
	for i, line in enumerate(string.splitlines()):
		parsed_line = {}
		parsed_line["ID"] = i + 1
		hands = line.split(": ")[1].split("; ")
		parsed_line["red"] = 0
		parsed_line["green"] = 0
		parsed_line["blue"] = 0
		for hand in hands:
			for cubes_of_color in hand.split(", "):
				cubes = cubes_of_color.split(" ")[0]
				color = cubes_of_color.split(" ")[1]
				if (color in ["red", "green", "blue"]):
					parsed_line[color] = max(parsed_line[color], int(cubes))
		parsed_input.append(parsed_line)
	return parsed_input

def possible_games(games : list, red_cubes : int, green_cubes : int, blue_cubes : int) -> list:
	possible = []
	for game in games:
		if game["red"] <= red_cubes:
			if game["green"] <= green_cubes:
				if game["blue"] <= blue_cubes:
					possible.append(game["ID"])
	return possible

def game_powers(game : list) -> list:
	powers = []
	for game in games:
		powers.append(game["red"] * game["green"] * game["blue"])
	return (powers)

games = parse_input(input_text)
print(sum(possible_games(games, 12, 13, 14)))
print(sum(game_powers(games)))
