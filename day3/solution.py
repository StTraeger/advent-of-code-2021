import collections


# Challenge 1
def find_most_and_least_digit(list_of_numbers, return_if_equal=None):
    list_of_digits = []
    for i in range(len(list_of_numbers)):
        list_of_digits.append(list_of_numbers[i])
    most_common_digits = collections.Counter(list_of_digits).most_common()
    if len(most_common_digits) == 1:
        return most_common_digits[0][1], most_common_digits[0][1]
    if most_common_digits[0][1] == most_common_digits[1][1] and return_if_equal:
        return return_if_equal, return_if_equal
    return most_common_digits[0][0], most_common_digits[-1][0]


def get_digits_for_index(input_list, idx):
    digits = []
    for i in range(len(input_list)):
        digits.append(input_list[i][idx])
    return digits


numbers = []

with open("input.txt") as file:
    for line in file:
        numbers.append([int(i) for i in line.rstrip()])

gamma_rate = []
epsilon_rate = []

for j in range(len(numbers[0])):
    digit_list = get_digits_for_index(numbers, j)
    gamma_rate.append(find_most_and_least_digit(digit_list)[0])
    epsilon_rate.append(find_most_and_least_digit(digit_list)[1])

epsilon_rate_int = int("".join([str(i) for i in epsilon_rate]), 2)
gamma_rate_int = int("".join([str(i) for i in gamma_rate]), 2)
print("Solution: " + str(gamma_rate_int * epsilon_rate_int))


# Challenge 2
# oxygen generator rating:
    # Most common bit
    # if equal -> 1
# co2 scrubber rating:
    # Least common bit
    # if equal -> 0
def calculate_rate(original_numbers, nr_digits_per_number, return_if_equal, least_common):
    remaining_elements = original_numbers.copy()
    indexes_to_remove = []
    index = 0

    while len(remaining_elements) >= 1 and index < nr_digits_per_number:
        indexes_to_remove = []
        # oxygen rating
        running_idx = len(remaining_elements)
        digit_list = get_digits_for_index(remaining_elements, index)
        most_xy_bit = find_most_and_least_digit(digit_list, return_if_equal=return_if_equal)[least_common]
        for i in range(running_idx):
            if digit_list[i] != most_xy_bit:
                indexes_to_remove.append(i)
        for j in sorted(indexes_to_remove, reverse=True):  # Note: Remove reverse to prevent indexOutOfBoundException
            remaining_elements.remove(remaining_elements[j])
        if len(remaining_elements) == 1:
            break
        index += 1
    return remaining_elements


oxygen_rating = calculate_rate(numbers, 12, 1, False)
print("Oxygen rating " + str(oxygen_rating))
oxygen_int = int("".join([str(i) for i in oxygen_rating[0]]), 2)

co2_rating = calculate_rate(numbers, 12, 0, True)
print("CO2 rating " + str(co2_rating))
co2_int = int("".join([str(i) for i in co2_rating[0]]), 2)
print("Solution " + str(oxygen_int * co2_int))
