def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = 66528
b = 52920

print(gcd(a,b))