import re

def get_user_info():
    name = input("Please enter your name: ")
    while not name or name.isdigit():
        name = input("Invalid input. Please enter your name: ")
    email = input("Please enter your email address: ")

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    is_valid_email = re.match(email_regex, email)
    if is_valid_email:
        print(f"Name: {name}")
        print(f"Email: {email}")
    else:
        while not is_valid_email:
            email = input("Invalid email. Please enter a valid email address: ")
            is_valid_email = re.match(email_regex, email)

        print(f"Name: {name}")
        print(f"Email: {email}")



get_user_info()
    