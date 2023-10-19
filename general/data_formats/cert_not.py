import cryptography
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Load your DER-encoded certificate
with open('2048b-rsa-example-cert.der', 'rb') as cert_file:
    cert_data = cert_file.read()

# Parse the certificate
certificate = x509.load_der_x509_certificate(cert_data, default_backend())

# Extract the public key
public_key = certificate.public_key()

print(public_key.public_numbers().n)
