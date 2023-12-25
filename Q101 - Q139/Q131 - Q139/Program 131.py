""" Q.Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same. """


def unique(numbers):
    # Use a dictionary to count occurrences of each number
    count_dict = {}

    # Count occurrences of each number in the list
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the unique number (occurs only once)
    for num, count in count_dict.items():
        if count == 1:
            return num


print(unique([0, 1, 1, 1, 1, 1, 1, 1]))
