# Daniel's + Lisy's Code

def menu_options():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


simp_password = ""


def encode_number(simp_password):
    encoded_password = ""
    for digit in simp_password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decode_number(simp_password):
    decoded_password = ""
    for digit in simp_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


if __name__ == '__main__':
    while True:
        menu_options()
        menu_option = input("Please enter an option: ")
        if menu_option == "1":
            simp_password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif menu_option == "2":
            if 'simp_password' in locals():
                print("The encoded password is " + encode_number(
                    simp_password) + ", and the original password is " + (simp_password))
            else:
                print("No password has been encoded yet.")
        else:
            break
