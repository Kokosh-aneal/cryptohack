from Crypto.Util.number import long_to_bytes, inverse

class Solver:
    def __init__(self, p, q, e):
        self.N = p * q
        self.e = e

    def solve(self, encrypted_flag, modulus, padding):
        a, b = padding
        # Step 2
        a_inv = inverse(a, self.N)
        # Step 3
        p_q = self.N
        # Step 4
        N_inv = inverse(p_q, self.N)
        # Step 5
        m = (b * N_inv) % self.N
        # Step 6
        flag = long_to_bytes(m)
        return flag

# Replace these values with the actual primes and exponent used in the challenge
p = ...  # Get the actual value
q = ...  # Get the actual value
e = 11  # This is given in the challenge

solver = Solver(p, q, e)

# Replace these values with the actual values obtained from the challenge
encrypted_flag = ...
modulus = ...
padding = ...

# Solve the challenge
flag = solver.solve(encrypted_flag, modulus, padding)
print("Decrypted Flag:", flag.decode())
