import random

# Generates a prime number
def generate_prime():
    while True:
        number = random.randint(1000, 10000)

        if check_prime(number):
            return number


# Checks if the number is a prime or not
def check_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    square_root = int(number ** 0.5) + 1
    for i in range(3, square_root, 2):
        if number % i == 0:
            return False

    return True


# Calculates the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Generates private and public key
def generate_keys():
    p = generate_prime()
    q = generate_prime()

    n = p * q

    euler_phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, euler_phi)
        if gcd(e, euler_phi) == 1:
            break

    d = pow(e, -1, euler_phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


# Saves key to file
def save_key(key, file):
    with open(file, 'w') as file:
        file.write(','.join(str(x) for x in key))



print("Generating RSA keys...")
public_key, private_key = generate_keys()
save_key(public_key, 'public_key.txt')
save_key(private_key, 'private_key.txt')
print("Public and private keys saved in separate files")

