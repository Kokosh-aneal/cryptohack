def extended_gcd_positive(a, b):
    if b == 0:
        return a, 1, 0
    nwd, u1, v1 = extended_gcd(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    if u < 0:
        u += b
    if v < 0:
        v += a

    return nwd, u, v

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    nwd, u1, v1 = extended_gcd(b, a % b)
    print(nwd, u1, v1)
    u = v1
    v = u1 - (a // b) * v1

    return nwd, u, v

# p = 26513
# q = 32321
# p = 26
# q = 15
p = 3
q = 13

print(extended_gcd_positive(p,q))