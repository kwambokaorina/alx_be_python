# pattern_drawing.py

# Prompt the user to input a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to keep track of rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side for each column in the row
    for col in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    # Move to the next row
    row += 1

