with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

race_times = [int(time) for time in input_lines[0].removesuffix("\n").split(": ")[1].split(" ") if time != ""]
record_distances = [int(distance) for distance in input_lines[1].removesuffix("\n").split(": ")[1].split(" ") if distance != ""]

def get_ways_to_beat(race_time : int, distance_record : int) -> list[int]:
	ways_to_beat : list[int] = []
	for button_time in range(race_time + 1):
		distance_traveled = (race_time - button_time) * button_time
		if distance_traveled > distance_record:
			ways_to_beat.append(button_time)
	return (ways_to_beat)

ways_to_beat_all_records = [get_ways_to_beat(race_times[i], record_distances[i]) for i in range(len(race_times))]

part1 = 1

for ways in ways_to_beat_all_records:
	part1 *= len(ways)

print("part1:", part1)

big_race_time = int("".join([str(number) for number in race_times]))
big_racord_distance = int("".join([str(number) for number in record_distances]))

ways_to_beat_big_record = get_ways_to_beat(big_race_time, big_racord_distance)

print("part2:", len(ways_to_beat_big_record))