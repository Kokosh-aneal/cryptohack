from Crypto.PublicKey import RSA

# with open("privacy_enhanced_mail.pem", 'rb') as f:
with open("bruce_rsa.pem", 'rb') as f:
    priv_key = RSA.import_key(f.read())

d = priv_key.dp
print(d)