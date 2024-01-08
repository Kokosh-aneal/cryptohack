def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calculate N and totient
N = p * q
phi_N = (p - 1) * (q - 1)
print(phi_N)

# Calculate the private key (d)
d = modinv(e, phi_N)

print("Private Key (d):", d)
