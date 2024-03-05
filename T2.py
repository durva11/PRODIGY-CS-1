def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)

