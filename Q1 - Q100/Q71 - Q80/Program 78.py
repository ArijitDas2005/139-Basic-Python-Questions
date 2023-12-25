""" Q. A website requires the users to input username and password to register. Write a program to check the validity of
password input by users. Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
  3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and willb check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example:--->
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""


import re


# Function to check if a password is valid
def is_valid_password(password):
    # Check the length of the password
    if 6 <= len(password) <= 12:
        # Check if the password matches all the criteria using regular expression
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False


# Initialize a list to store valid passwords
valid_passwords = []

# Accept input from the user as comma-separated passwords
passwords = input("Enter passwords separated by commas: ").split(',')

# Iterate through the passwords and check their validity
for psw in passwords:
    if is_valid_password(psw):
        valid_passwords.append(psw)

# Print the valid passwords separated by commas
print(','.join(valid_passwords))
