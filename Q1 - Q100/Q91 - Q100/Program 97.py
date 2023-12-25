""" Q.Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "shkspr* """


def replace_vowels(string, char):
    vowels = "AEIOUaeiou"  # List of vowels to be replaced
    for vowel in vowels:
        string = string.replace(vowel, char)  # Replace each vowel with specified character
    return string


print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
