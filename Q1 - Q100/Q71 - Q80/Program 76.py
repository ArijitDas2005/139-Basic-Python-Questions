"""Q. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""


def remove_duplicates_and_sort(input_string):
  # Split the input string into a list of words
  words = input_string.split()

  # Remove duplicates by converting the list to a set and then back to a list
  unique_words = list(set(words))

  # Sort the list alphanumerically
  unique_words.sort()

  # Print the result
  print(" ".join(unique_words))


# Get input from the user
input_sequence = input("Enter a sequence of whitespace separated words: ")

# Call the function with the input and print the result
remove_duplicates_and_sort(input_sequence)
