def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    # Adjust shift for decryption
    if not encrypt:
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' to encrypt or 'D' to decrypt.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (positive integer): "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()