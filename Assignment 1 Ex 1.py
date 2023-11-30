def multiply_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Example usage:
result = multiply_or_sum(20, 30)
print(result)  # Output will be 1200, so it returns their sum
