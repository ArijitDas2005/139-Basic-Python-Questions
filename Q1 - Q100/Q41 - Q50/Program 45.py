# Q.Write a Python program to print all happy numbers between 1 and 100.


def is_happy_number(number):
    seen = set()

    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(i) ** 2 for i in str(number))

    return number == 1


happy_numbers = []

for num in range(1, 101):
    if is_happy_number(num):
        happy_numbers.append(num)

print("Happy Numbers between 1 and 100:")
print(happy_numbers)
