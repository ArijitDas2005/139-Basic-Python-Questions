# Q. Write a Python program to check order of character in string using OrderedDict().


from collections import OrderedDict


def check_order(input_string, pattern):
    """Checks if the characters in the input_string follow the same order as the pattern.

      Args:
        input_string: The string to check.
        pattern: The pattern to match.

      Returns:
        True if the input_string matches the pattern, False otherwise.
      """
    my_dict = OrderedDict.fromkeys(input_string)  # Create an OrderedDict preserving character order
    pattern_length = 0  # Counter for characters matching the pattern

    for key in my_dict.keys():    # Iterate through characters in the OrderedDict
        if key == pattern[pattern_length]:  # Check if the current character matches the pattern
            pattern_length += 1   # If it matches, move to the next character in the pattern
            if pattern_length == len(pattern):  # If all characters in the pattern are matched, return True
                return True
        else:   # If a character doesn't match, the string doesn't follow the pattern
            return False

    return False  # If the loop completes without matching all characters in the pattern, return False


# Example usage:
input_string = "engineers rock"
pattern = "er"

if check_order(input_string, pattern):
    print("The string follows the pattern.")
else:
    print("The string does not follow the pattern.")
