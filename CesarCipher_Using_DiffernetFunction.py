logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Here is the Encryption function
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



#Here is the Decryption Function
def decrypt(text,shift):
    decrypted_Text=""
    for i in text:
        position=alphabet.index(i)
        new_position=position-shift
        if new_position<0:
            new_position+=position
            new_letter=alphabet[new_position]
        else:
            new_letter=alphabet[new_position]
        decrypted_Text+=new_letter
    print(f"The Decoded text is {decrypted_Text}")

#Here We call the funciton
#If your choose any function it should call the corresponding function


if direction=="encode":
    encrypt(text, shift)
elif direction=="decode":       
    decrypt(text, shift)

else:     
    print("Wrong Choice")
