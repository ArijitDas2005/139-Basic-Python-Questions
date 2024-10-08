""" Q.Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
number).
2. If the number cannot be divided evenly by 4, simply return the number.
Examples
amplify(4) ➞ [1, 2, 3, 40]
amplify(3) ➞ [1, 2, 3]
amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21,
22, 23, 240, 25]
Notes
 (i)The given integer will always be equal to or greater than 1.
 (ii)Include the number (see example above).
 (iii)To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult,
 just solve the challenge any way you can. """


def amplify(num):
    # Use a list comprehension to generate the list
    return [n * 10 if n % 4 == 0 else n for n in range(1, num + 1)]


print(amplify(3))
print(amplify(25))
