# Loads key
def load_key(file):
    with open(file, 'r') as file:
        data = file.read().split(',')
        key = tuple(int(x) for x in data)
    return key


# Decrypts the encrypted text using the private key
def decrypt(encrypted_text, private_key):
    n, d = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]

    return ''.join(decrypted_text)


with open('encrypted_text.txt', 'r') as file:
    encrypted_text = [int(x) for x in file.read().split(',')]
private_key = load_key('private_key.txt')
decrypted_text = decrypt(encrypted_text, private_key)
print("Decrypted text:", decrypted_text)