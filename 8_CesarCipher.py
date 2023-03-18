alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Here is the Encrypty function
def encrypt(text,shift):
    encrypted_Text=""
    for i in text:
        position=alphabet.index(i)
        new_position=position+shift
        if new_position>25:
            new_position-=position
            new_letter=alphabet[new_position]
        else:
            new_letter=alphabet[new_position]

        encrypted_Text+=new_letter
    print(f"The encoded text is {encrypted_Text}")

encrypt(text,shift)
    