def display_divisible_by_5(lst):
    for num in lst:
        if num % 5 == 0:
            print(num, end=' ')

given_list = [10, 20, 33, 46, 55]
print("Numbers divisible by 5 in the given list:", end=' ')
display_divisible_by_5(given_list)
