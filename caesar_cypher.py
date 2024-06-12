import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#The main function to encrypt or decrypt
def caeser(direction, text, shift):
    modified_text = []
    if direction == "decode":
        shift = -shift
    for letter in text:
        if letter in alphabet:
            x = alphabet.index(letter)
            new_index = int((x + shift) % 26)
            modified_text.append(alphabet[new_index])
        else:
            modified_text.append(letter)
    print(''.join(modified_text))
#A while construct otherwise the goddamn code won't take new values
while True: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #To handle inputs from dumb users count: 1
    if direction not in ['encode', 'decode']:
        print("Invalid direction! Please type 'encode' or 'decode'.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #Calling the main function
    caeser(direction=direction, text=text, shift=shift)
    #To check for the repeatation of the program
    repeat = input("Do you wanna run this program again?\nPlease type 'yes' if yes, Type 'no' if no.\n").lower()
    if repeat == "no":
        sys.exit("Hope I helped :)")
    elif repeat == "yes":
        continue
    #To handle inputs from dumb users count: 2
    else:
        sys.exit("Invalid input! Exiting...")