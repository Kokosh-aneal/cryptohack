from Crypto.PublicKey import RSA

# Load the public PEM-encoded key (replace 'public_key.pem' with your key file)
with open('transparency.pem', 'rb') as key_file:
    key_data = key_file.read()

# Parse the PEM-encoded key
public_key = RSA.import_key(key_data)

# Extract the modulus as a decimal integer
modulus = public_key.n
print(modulus)