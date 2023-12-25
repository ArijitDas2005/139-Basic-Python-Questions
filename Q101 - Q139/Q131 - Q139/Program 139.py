""" Q.Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its 
lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg." """


def ascii_capitalize(input_str):
    result = ""

    for char in input_str:
        if ord(char) % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()

    return result


print(ascii_capitalize("THE LITTLE MERMAID"))
