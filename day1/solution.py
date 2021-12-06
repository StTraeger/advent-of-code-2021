def calc_sliding_window(elements, window_size):
    increase_count = 0
    for i in range(len(elements) - (window_size - 1)):
        if sum(elements[i:i + window_size]) < sum(elements[i + 1:i + 1 + window_size]):
            increase_count += 1
    return increase_count


input_numbers = list(map(int, [line.rstrip() for line in open("input.txt")]))

# Challenge 1
print("Numbers increased, challenge 1:")
print(calc_sliding_window(input_numbers, 1))

# Challenge 2
print("Windows increased, challenge 2:")
print(calc_sliding_window(input_numbers, 3))
