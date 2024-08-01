def encrypt(text, shift):
    result = ""
    
    # Traverse the plain text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt or (q)uit? ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter shift value: "))

            if choice == 'e':
                encrypted_message = encrypt(message, shift)
                print("Encrypted message:", encrypted_message)
            elif choice == 'd':
                decrypted_message = decrypt(message, shift)
                print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
