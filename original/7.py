with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.readlines()

hands = [line.split(" ") for line in input_lines]

card_icons = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def card_value(cards1 : str) -> int:
	value = 0
	for i in range(5):
		value *= len(card_icons)
		value += len(card_icons) - card_icons.index(cards1[i])
	return value

def get_kind(cards : str) -> int:
	found_letters : str = ""
	jokers = 0
	times : list[int] = []
	for char in cards:
		if char == 'J':
			jokers += 1
		elif char not in found_letters:
			found_letters += char
			times.append(1)
		else:
			times[found_letters.index(char)] += 1
	if len(times) > 0:
		times.sort(reverse=True)
		times[0] += jokers
	else:
		times.append(jokers)
		found_letters += 'J'
	if len(found_letters) == 1:
		return 7
	if len(found_letters) == 2:
		if 4 in times:
			return 6
		return 5
	if len(found_letters) == 3:
		if 3 in times:
			return 4
		return 3
	if len(found_letters) == 4:
		return 2
	if len(found_letters) == 5:
		return 1
	return 0

def value_hand(hand : list[str]) -> int:
	return get_kind(hand[0]) * 1000000000 + card_value(hand[0])

hands.sort(key = value_hand)

print(sum([int(hand[1]) * (rank + 1) for rank, hand in enumerate(hands)]))