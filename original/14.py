with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

platform = input_lines

def tilt_north():
	for y in range(len(platform)):
		for x in range(len(platform[y])):
			if (platform[y][x] == 'O'):
				i = 1
				while i <= y and platform[y-i][x] == '.':
					i += 1
				i -= 1
				platform[y] = platform[y][:x] + '.' + platform[y][x+1:]
				platform[y-i] = platform[y-i][:x] + 'O' + platform[y-i][x+1:]
def tilt_east():
	for ry in range(len(platform)):
		y = len(platform) - ry - 1
		for rx in range(len(platform[y])):
			x = len(platform[y]) - rx - 1
			if (platform[y][x] == 'O'):
				i = 1
				while i+x < len(platform[y]) and platform[y][x+i] == '.':
					i += 1
				i -= 1
				platform[y] = platform[y][:x] + '.' + platform[y][x+1:]
				platform[y] = platform[y][:x+i] + 'O' + platform[y][x+i+1:]
def tilt_south():
	for ry in range(len(platform)):
		y = len(platform) - ry - 1
		for rx in range(len(platform[y])):
			x = len(platform[y]) - rx - 1
			if (platform[y][x] == 'O'):
				i = 1
				while i+y < len(platform) and platform[y+i][x] == '.':
					i += 1
				i -= 1
				platform[y] = platform[y][:x] + '.' + platform[y][x+1:]
				platform[y+i] = platform[y+i][:x] + 'O' + platform[y+i][x+1:]
def tilt_west():
	for y in range(len(platform)):
		for x in range(len(platform[y])):
			if (platform[y][x] == 'O'):
				i = 1
				while i <= x and platform[y][x-i] == '.':
					i += 1
				i -= 1
				platform[y] = platform[y][:x] + '.' + platform[y][x+1:]
				platform[y] = platform[y][:x-i] + 'O' + platform[y][x-i+1:]
def get_north_load():
	load = 0
	for y in range(len(platform)):
		for x in range(len(platform[y])):
			if (platform[y][x] == 'O'):
				load += len(platform) - y
	return (load)


# tilit_north()
# print(get_north_load())

history = []

cycles = 1000000000
while cycles > 0:
	tilt_north()
	tilt_west()
	tilt_south()
	tilt_east()
	if platform in history:
		break
	cycles -= 1
	history.append(platform.copy())
	# print(*platform,"",sep="\n")

history_loop = history[history.index(platform):]
platform = history_loop[(cycles - 1) % len(history_loop)]
print(get_north_load())