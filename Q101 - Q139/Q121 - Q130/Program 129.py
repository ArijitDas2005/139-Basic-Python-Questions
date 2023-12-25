""" Q.Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
   (i)The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is
(5+1+2)/3(number of digits) = 8/3=2).
  (ii)The mean will always be an integer. """


def mean(n):
    # Convert the number to a string to iterate through its digits
    n_str = str(n)

    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in n_str)

    # Calculate the mean by dividing the sum by the number of digits
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count

    return int(digit_mean)


print(mean(12345))
