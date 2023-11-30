def check_first_last_same(lst):
    return lst[0] == lst[-1]

number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]

result_x = check_first_last_same(number_x)
result_y = check_first_last_same(number_y)

print(f"For number_x: First and last numbers are the same? {result_x}")
print(f"For number_y: First and last numbers are the same? {result_y}")
