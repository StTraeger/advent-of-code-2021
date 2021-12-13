import collections


# Challenge 1
def find_most_and_least_digit(list_of_numbers, return_if_equal=None):
    list_of_digits = []
    for i in range(len(list_of_numbers)):
        list_of_digits.append(list_of_numbers[i])
    most_common_digits = collections.Counter(list_of_digits).most_common()
    if most_common_digits[0][1] == most_common_digits[1][1] and return_if_equal:
        return return_if_equal
    return most_common_digits[0][0], most_common_digits[-1][0]


numbers = []

with open("input.txt") as file:
    for line in file:
        numbers.append([int(i) for i in line.rstrip()])

gamma_rate = []
epsilon_rate = []

for j in range(len(numbers[0])):
    digits = []
    for i in range(len(numbers)):
        digits.append(numbers[i][j])
    gamma_rate.append(find_most_and_least_digit(digits)[0])
    epsilon_rate.append(find_most_and_least_digit(digits)[1])

epsilon_rate_int = int("".join([str(i) for i in epsilon_rate]), 2)
gamma_rate_int = int("".join([str(i) for i in gamma_rate]), 2)
print("Solution: " + str(gamma_rate_int * epsilon_rate_int))


# Challenge 2
def number_match(number, position, criteria, return_if_equal):
    return True if number[position] == criteria else False




