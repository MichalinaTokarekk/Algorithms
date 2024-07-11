def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Przykład użycia
text = "Hello, World!"
shift = 3
encrypted_text = caesar_encrypt(text, shift)
print(f'Szyfrogram: {encrypted_text}')

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f'Odszyfrowany tekst: {decrypted_text}')
