"""Q.Write a program to compute the frequency of the words from the input. The output should output after sorting the
key alphanumerically. Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1"""


input_sentence = input("Enter a sentence: ")

# Split the sentence into words
words = input_sentence.split()

# Create a dictionary to store word frequencies
word_freq = {}

# Count word frequencies
for word in words:
    # Remove punctuation (., ?) from the word
    word = word.strip('.,?')

    # Convert the word to lowercase to ensure case-insensitive counting
    word = word.lower()

    # Update the word frequency in the dictionary
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the words alphanumerically
sorted_words = sorted(word_freq.items())

# Print the word frequencies
for word, frequency in sorted_words:
    print(f"{word}:{frequency}")
