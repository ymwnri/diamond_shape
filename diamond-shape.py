# Program: Diamond Shape
# Features: Takes an odd integer input and prints a diamond shape pattern
# Procedure:
# 1. Take an odd integer input
# 2. Check if the input is odd
# 3. Print the diamond shape pattern
# 4. Print result

def print_diamond_shape(n):
    """Print a diamond shape pattern.

    Args:
        n (int): The size of the diamond.
    """
    # Check if the input is odd
    if n % 2 == 0:
        print("Please enter an odd number.")
        return

    middle = n // 2

    # Top half of the diamond
    for i in range(middle + 1):
        spaces = " " * (middle - i)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    # Bottom half of the diamond
    for i in range(middle - 1, -1, -1):
        spaces = " " * (middle - i)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

# Start of the program
n = int(input("Enter an odd number: "))
print_diamond_shape(n)
