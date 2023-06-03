
# Loads key
def load_key(file):
    with open(file, 'r') as file:
        data = file.read().split(',')
        key = tuple(int(x) for x in data)
    return key


# Encrypts the text using the public key
def encrypt(text, public_key):
    n, e = public_key
    encrypted_text = [pow(ord(char), e, n) for char in text]

    return encrypted_text

text = input("Enter the text to encrypt: ")

public_key = load_key('public_key.txt')
encrypted_text = encrypt(text, public_key)

with open('encrypted_text.txt', 'w') as file:
    file.write(','.join(str(x) for x in encrypted_text))

print("Text encrypted and saved in a secure form")