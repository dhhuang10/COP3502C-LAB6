# Daniel's Code
def menu_options():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_number(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_number(password):
    pass

if __name__ == '__main__':
    while True:
        menu_options()
        menu_option = input("Please enter an option: ")
        if menu_option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif menu_option == "2":
            print("The encoded password is " + encode_number(password) +", and the original password is " + password)
        else:
            break