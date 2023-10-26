
def encode(password):
    password = str(password)
    decoded = ""
    for i in range(0,8):
        value = int(password[i]) + 3
        decoded = decoded + str(value)
    return decoded

def quit_program():
    exit()

if __name__ == '__main__':
    while True:
        print("Menu\n-----------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            enter_encoded = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            enter_encoded = encode(enter_encoded)
        elif option == 2:
            decoded_value = decode(enter_encoded)
            print("the encoded password is " + str(enter_encoded) + ", and the original password is " + str(decoded_value))
        elif option == 3:
            quit_program()





