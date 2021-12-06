# Start horizontal=0 and depth=0

# Challenge 1
# forward x -> horizontal + x
# down x -> depth + x
# up x -> depth - x
d = {'forward': 0, 'down': 0, 'up': 0}
with open('input.txt') as file:
    for line in file:
        (key, val) = line.split()
        d[key] += int((key, val)[1])

horizontal = d['forward']
depth = d['down'] - d['up']

print("Solution challenge 1: " + str(horizontal * depth))

# Challenge 2
# forward x -> horizontal + x && depth = depth + (depth * aim)
# up x -> aim - x
# down x -> aim + x
horizontal = 0
depth = 0
aim = 0
with open('input.txt') as file:
    for line in file:
        (key, val) = line.split()
        if key == 'forward':
            horizontal += int(val)
            depth = depth + int(val) * aim
        if key == 'up':
            aim -= int(val)
        if key == 'down':
            aim += int(val)

print("Solution challenge 2:" + str(horizontal * depth))
