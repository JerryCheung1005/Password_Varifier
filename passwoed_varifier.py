MIN_LENGTH = 10
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():

    """Program to get and check a user's password."""

    # Print the rules
    print('''The rules for creating a password here are:
    The minimum length should be of 10 characters including
    at least one numerical value, one uppercase English alphabet, 
    one lowercase English alphabet, and one symbol
    and no 3 consecutive chars 
    ''')

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    # Input the password
    password = input("Enter a password: ")
    Try_time = 1
    while not is_valid_password(password):
        Try_time += 1
        print("Breakdown of the password")
        print("Length of your password is: ", str(len(password)))
        print("Invalid password. Try again please.")
        if 2 <= Try_time <= 5:
            while True:
                answer = input("Want to set your password? Type 1 for yes and 0 for no:")
                if answer == 1:
                    pass

        password = input("Enter a password: ")
        if Try_time == 5:
            print("You have exceed the max number of chances! Bye.")
            print('''
            
            
            ''')
            print('''The rules for creating a password here are:
                The minimum length should be of 10 characters including
                at least one numerical value, one uppercase English alphabet, 
                one lowercase English alphabet, and one symbol
                and no 3 consecutive chars 
                ''')
            break
    if is_valid_password(password):
        print("Your " + str(
            len(password)) + " character password is valid: " + password)
    else:
        pass


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # if length is wrong, return False
    if len(password) < MIN_LENGTH:
        return False

    # Calculate lower, upper, digit and special char
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # count each kind of character (use str methods like isdigit)
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    # if any of the 'normal' counts are zero, return False
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # If have special character, return False
    if count_special != 0:
        print("Please don't put 3 consecutive identical chars.")
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()