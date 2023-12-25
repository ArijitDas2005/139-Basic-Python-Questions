""" Q.Create a function that squares every digit of a number.
Examples:--->
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer."""


def square_digits(n):
    # Convert the number to a string to iterate through its digits
    num_str = str(n)

    # Initialize an empty string to store the squared digits
    result_str = ""

    # Iterate through the digits
    for digit in num_str:
        # Square the digit and convert it back to an integer
        squared_digit = int(digit) ** 2

        # Append the squared digit to the result string
        result_str += str(squared_digit)

    return int(result_str)


print(square_digits(3212))
