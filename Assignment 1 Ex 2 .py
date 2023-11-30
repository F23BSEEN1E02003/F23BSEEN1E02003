def print_sum_of_previous(current):
    previous = 0
    for i in range(current):
        print(f"Current number: {i}, Sum with previous: {i + previous}")
        previous = i

# Iterating the first 10 numbers
print_sum_of_previous(10)
