""" Q.Create a function that sorts a list and removes all duplicate items from it.
Examples:--->
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]"""


def setify(lst):
    unique_set = set(sorted(lst))

    # Convert the set back to a list and return it
    return list(unique_set)


print(setify([5, 7, 8, 9, 10, 15]))
