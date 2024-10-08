""" Q.Write a function, that replaces all vowels in a string with a specified vowel.
Examples:--->
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel."""


def vow_replace(string, vowel):
    vowels = "aeiou"
    result = ""

    for char in string:
        if char in vowels:
            result += vowel
        else:
            result += char

    return result


print(vow_replace("apples and bananas", "u"))
print(vow_replace("cheese casserole", "o"))
print(vow_replace("stuffed jalapeno poppers", "e"))
