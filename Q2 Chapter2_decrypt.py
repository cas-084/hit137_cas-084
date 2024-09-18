# chapter2_decrypt.py

# Function to decrypt the ciphered quote using shift key 's'
def decrypt_caesar_cipher(ciphered_text, shift_key):
    decrypted_text = ''
    for char in ciphered_text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                decrypted_text += chr(((ord(char) - ord('A') - shift_key) % 26) + ord('A'))
            # Handle lowercase letters
            elif char.islower():
                decrypted_text += chr(((ord(char) - ord('a') - shift_key) % 26) + ord('a'))
        else:
            # If it's not a letter, don't change it (space, punctuation, etc.)
            decrypted_text += char
    return decrypted_text

# Example ciphered quote (you can replace this with any cryptogram)
ciphered_quote = "VZ FNYSVF UZINGVRAG NAQ N YVGGYR VAFPHER V ZNQR IVFGNKRF V NZ BHG BS PBAGEBY"

# Try different shift keys and print decrypted text
for shift in range(1, 26):  # Caesar Cipher usually has 26 possible shifts
    print(f"Shift Key {shift}: {decrypt_caesar_cipher(ciphered_quote, shift)}\n")

