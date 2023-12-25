# Q.Write a Python program to print even numbers in a list.


# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a list comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the even numbers
print("Even numbers in the list:", even_numbers)
