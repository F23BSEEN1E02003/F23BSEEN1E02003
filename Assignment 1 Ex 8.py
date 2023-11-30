list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Filtering odd numbers from list1
odd_numbers = [num for num in list1 if num % 2 != 0]

# Filtering even numbers from list2
even_numbers = [num for num in list2 if num % 2 == 0]

# Combining the odd numbers from list1 and even numbers from list2 into a new list
new_list = odd_numbers + even_numbers

print("New list containing odd numbers from list1 and even numbers from list2:")
print(new_list)

