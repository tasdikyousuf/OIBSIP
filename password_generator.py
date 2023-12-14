# secrets module has been imported instead of random
import secrets
import string

#defining the function with three parameters: length of the password, availability condition for digits and special (user must pick at least one)
def password_generator(length, digit, special):
    # store sets of ASCII characters representing uppercase and lowercase letters, digits, and special characters
    pass_letters = string.ascii_letters
    pass_digits = string.digits
    pass_special = string.punctuation

    # an empty string to store the generated password
    password = ''

    # conditions based on user preference

    # user picked both
    if digit == "y" and special == "y":
        pass_characters = pass_letters + pass_digits + pass_special
        for i in range(length):
            password = password + ''.join(secrets.choice(pass_characters))
        print(password)

    # user picked digits
    elif digit == "y" and special != "y":
        pass_characters = pass_letters + pass_digits
        for i in range(length):
            password = password + ''.join(secrets.choice(pass_characters))
        print(password)

    # user picked special characters
    elif special == "y" and digit != "y":
        pass_characters = pass_letters + pass_special
        for i in range(length):
            password = password + ''.join(secrets.choice(pass_characters))
        print(password)


# user input
pass_length = int(input("Enter Total Password length you want: "))

# a warning message to make the user choose at least one criterion
print("Warning: you must select letters and at least one more criteria to generate a password.")

# input for criteria
want_digit = input("press y if you want numbers or press enter: ")
want_special = input("press y if you want special character or press enter: ")

# calling the function to show a generated password
password_generator(pass_length, want_digit, want_special)