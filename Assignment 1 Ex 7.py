def is_palindrome(number):
    # Convert number to string for easier manipulation
    num_str = str(number)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Check if the original number is equal to its reverse
    return num_str == reversed_str

# Example usage:
number = 121  # You can change this number to test different values
if is_palindrome(number):
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")
