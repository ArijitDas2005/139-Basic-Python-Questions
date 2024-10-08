""" Q.Create a function that takes a list of strings and return a list, sorted from shortest to longest.
Examples
sort_by_length(["Google", "Apple", "Microsoft"]) ➞ ["Apple", "Google", "Microsoft"]
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) ➞ ["Raphael",
"Leonardo", "Donatello", "Michelangelo"]
sort_by_length(["Turing", "Einstein", "Jung"]) ➞ ["Jung", "Turing", "Einstein"]
Notes
All test cases contain lists with strings of different lengths, so you won't have to deal"""


def sort_by_length(lst):
    # Sort the list of strings based on their lengths
    # The 'key=len' argument specifies that the sorting should be based on the length of each string
    return sorted(lst, key=len)


print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
