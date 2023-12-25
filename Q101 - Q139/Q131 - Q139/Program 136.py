""" Q.Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
"D": 1,
"B": 2
"C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]
dict_to_list({
"likes": 2,
"dislikes": 3,
"followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
Notes
Return the elements in the list in alphabetical order. """


def dict_to_list(input_dict):
    # Sort the dictionary by keys in alphabetical order
    sorted_dict = sorted(input_dict.items())

    # Convert the sorted dictionary to a list of tuples
    result = [(key, value) for key, value in sorted_dict]

    return result


print(dict_to_list({
    "D": 1,
    "B": 2,
    "C": 3
}))

print(dict_to_list({
    "likes": 2,
    "dislikes": 3,
    "followers": 10
}))
