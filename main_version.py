import secrets
import string
import time


def generate_password():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    final_password = lower_case + upper_case + numbers + symbols

    final_password = "".join(secrets.choice(final_password) for i in range(user_password_length))
    print("Your new password is: " + final_password)


print("Welcome to the Secure Password Generator ")
time.sleep(1)
#input length of password
user_password_length = int(input("\nPlease enter amount of characters to generate a password: "))
time.sleep(1)
generate_password()
time.sleep(1)

print("Thank you for using HSPG")
