import secrets
import string

def password_generator(length, digit, special):
    pass_letters = string.ascii_letters
    pass_digits = string.digits
    pass_special = string.punctuation

    password = ''

    if digit == "y" and special == "y":
        pass_characters = pass_letters + pass_digits + pass_special
        for i in range(length):
            password += secrets.choice(pass_characters)
        print(password)

    elif digit == "y" and special != "y":
        pass_characters = pass_letters + pass_digits
        for i in range(length):
            password += secrets.choice(pass_characters)
        print(password)

    elif special == "y" and digit != "y":
        pass_characters = pass_letters + pass_special
        for i in range(length):
            password += secrets.choice(pass_characters)
        print(password)


pass_length = int(input("Enter the total password length you want: "))

print("Warning: You must select letters and at least one more criterion to generate a password.")

want_digit = input("Press 'y' if you want numbers or press enter: ")
want_special = input("Press 'y' if you want special characters or press enter: ")

password_generator(pass_length, want_digit, want_special)
