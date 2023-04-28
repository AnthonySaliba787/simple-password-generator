import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
f = open("SavedPasswords.txt", "a")


def generate_random_password():
    length = 0

    # Taking the password length
    while length <= 0:
        try:
            length = int(input("Enter password length: "))
        except ValueError:
            print("Oops! That was not a valid number, please try again..")

    # Customization
    while True:
        try:
            alphabets_count = int(input("Enter alphabets count: "))
            break
        except ValueError:
            print("Oops! That was not a valid number, please try again..")

    while True:
        try:
            digits_count = int(input("Enter digits count: "))
            break
        except ValueError:
            print("Oops! That was not a valid number, please try again..")

    while True:
        try:
            special_characters_count = int(input("Enter special characters count: "))
            break
        except ValueError:
            print("Oops! That was not a valid number, please try again..")

    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("Operation failed: Total characters count is greater than the password length!")
        input("Press any key to exit..")
        return

    # Password initialized
    password = []

    # Password begins forming
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    # If the total characters is less than the length, populate it with random characters
    if characters_count < length:
        # First layer of security
        for i in range(0, 100):
            random.shuffle(characters)

        # Completing the password
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    # Second layer of security
    for i in range(0, 100):
        random.shuffle(password)

    print("\nThe password is:")
    print("".join(password))

    # Checking password health
    if length < 8:
        print("Password strength: Weak")
    elif 8 <= length < 16:
        print("Password strength: Moderate")
    else:
        print("Password strength: Strong")

    while True:
        is_saved = input("Would you like to save this password locally? (Y/N): ")

        if is_saved == "Y" or is_saved == "y" or is_saved == "yes" or is_saved == "Yes":
            # Saving password in a local text file
            f.write("".join(password))
            f.write("\n")
            f.close()

            print("Password has been saved successfully!")
            input("Press any key to exit..")
            break
        elif is_saved == "N" or is_saved == "n" or is_saved == "no" or is_saved == "No":
            print("Password discarded!")
            input("Press any key to exit..")
            break
        else:
            print("I'm sorry, I did not understand this input.")


generate_random_password()
