""" Q.What does the code do with the list writeyourcodehere = [1, 2, 3, 4, 5, 6]? Explain the purpose of the code
following the list declaration, particularly the use of unpacking with variables first, *middle, and last. What will be
the output when the code is executed, and why?"""


writeyourcodehere = [1, 2, 3, 4, 5, 6]
# Unpack the list into variables
first, *middle, last = writeyourcodehere

print(first)
print(middle)
print(last)
