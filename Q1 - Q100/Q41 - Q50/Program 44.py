# Q.Write a Python program to check if the given number is Happy Number.


def is_happy_number(number):
    seen = set()  # To store previously seen numbers

    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(i) ** 2 for i in str(number))

    return number == 1


# Test the function with a number
num = int(input("Enter a number: "))
if is_happy_number(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")
