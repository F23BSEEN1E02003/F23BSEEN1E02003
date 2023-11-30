def print_even_index_chars(string):
    for i in range(0, len(string), 2):
        print(string[i], end=' ')

user_input = input("Enter a string: ")
print("Characters at even index:", end=' ')
print_even_index_chars(user_input)
