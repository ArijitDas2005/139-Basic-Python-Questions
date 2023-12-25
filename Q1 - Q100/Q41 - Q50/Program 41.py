# Q.Write a Python Program to Remove Punctuation From a String.


# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# To take input from the user
my_str = input("Enter a string: ")

# remove punctuation from the string
no_punctuations = ""
for char in my_str:
    if char not in punctuations:
        no_punctuations = no_punctuations + char

# display the unpunctuated string
print(no_punctuations)
