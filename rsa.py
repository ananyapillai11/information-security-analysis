import math

# Defining p and q (prime numbers)
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

# Defining n
n = p * q
print("n =", n)

# Totient calculation
phi = (p - 1) * (q - 1)
e = 2

while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

print("e =", e)
k = 2
d = ((k * phi) + 1) / e
print("d =", d)

print(f'Public key: {e, n}')
print(f'Private key: {d, n}')

# Plain text
msg = int(input("Enter the original message: "))
print(f'Original message: {msg}')

# Encryption
c = pow(msg, e)
c = math.fmod(c, n)
print(f'Encrypted message: {c}')

# Decryption
M = pow(c, d)
M = math.fmod(M, n)
print(f'Decrypted Message: {M}')
