import numpy

with open("input.txt", "r") as input_file:
	input_lines : list[str] = input_file.read().split("\n")

POS = 0
VEL = 1
X = 0
Y = 1
Z = 2

def parse_hailstone(line : str):
	position, velocity = line.split(" @ ")
	x, y, z = map(float, position.split(", "))
	vx, vy, vz = map(float, velocity.split(", "))
	return ((x, y, z), (vx, vy, vz))

def is_in_future(x, y, hailstone):
	return numpy.sign(y - hailstone[POS][Y]) == numpy.sign(hailstone[VEL][Y]) and numpy.sign(x - hailstone[POS][X] ) == numpy.sign(hailstone[VEL][X])
	
hailstones = [parse_hailstone(line) for line in input_lines]

part1 = 0

MIN = 200000000000000
MAX = 400000000000000

for i in range(len(hailstones)):
	for j in range(i + 1, len(hailstones)):
		hailstone1 = hailstones[i]
		hailstone2 = hailstones[j]
		(px1, py1, _), (vx1, vy1, _) = hailstone1
		(px2, py2, _), (vx2, vy2, _) = hailstone2
		try:
			y = (px2 - (vx2 / vy2 * py2) + (vx1 / vy1 * py1) - px1) / (
                    vx1 / vy1 - vx2 / vy2
                )
			x = ((y - py1) / vy1) * vx1 + px1
		except:
			continue
		if x == None or y == None:
			continue
		if (MIN <= x <= MAX) and (MIN <= y <= MAX):
			if is_in_future(x, y, hailstone1) and is_in_future(x, y, hailstone2):
				part1 += 1
print(part1)

import z3

px = z3.Real("px")
py = z3.Real("py")
pz = z3.Real("pz")
vx = z3.Real("vx")
vy = z3.Real("vy")
vz = z3.Real("vz")

solver = z3.Solver()

for i in range(len(hailstones)):
	(hpx, hpy, hpz), (hvx, hvy, hvz) = hailstones[i]
	c_i = z3.Real(f"c_{i}")
	solver.add(hpx + hvx * c_i == px + vx * c_i)
	solver.add(hpy + hvy * c_i == py + vy * c_i)
	solver.add(hpz + hvz * c_i == pz + vz * c_i)

solver.check()
model = solver.model()
print(model[px] + model[py] + model[pz])