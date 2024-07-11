def transpose_encrypt(text, key):
    ciphertext = [''] * key
    for column in range(key):
        current_index = column
        while current_index < len(text):
            ciphertext[column] += text[current_index]
            current_index += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key):
    num_of_columns = int(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_columns
    column = 0
    row = 0
    for symbol in ciphertext:
        plaintext[column] += symbol
        column += 1
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1
    return ''.join(plaintext)

# Przykład użycia
text = "Hello, World!"
key = 5
encrypted_text = transpose_encrypt(text, key)
print(f'Szyfrogram: {encrypted_text}')

decrypted_text = transpose_decrypt(encrypted_text, key)
print(f'Odszyfrowany tekst: {decrypted_text}')
