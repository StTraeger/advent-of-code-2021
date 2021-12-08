# Challenge 1

numbers = []

with open("input.txt") as file:
    for line in file:
        numbers.append([int(i) for i in line.rstrip()])

gamma_rate = []
epsilon_rate = []

for j in range(len(numbers[0])):
    ones = 0
    zeros = 0
    for i in range(len(numbers)):
        if numbers[i][j] == 0:
            zeros += 1
        if numbers[i][j] == 1:
            ones += 1
    if ones > zeros:
        gamma_rate.append(1)
        epsilon_rate.append(0)
    if ones < zeros:
        gamma_rate.append(0)
        epsilon_rate.append(1)

epsilon_rate_int = "".join([str(i) for i in epsilon_rate])
gamma_rate_int = "".join([str(i) for i in gamma_rate])
print("Solution: " + str(int(gamma_rate_int, 2) * int(epsilon_rate_int, 2)))

# Challenge 2

