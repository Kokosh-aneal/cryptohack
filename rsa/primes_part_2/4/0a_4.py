from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from factordb import factordb

# Get vulnerable key and extract parameters
for i in range(1,50):
    vuln_key = RSA.import_key(open(f"{i}.pem", 'r').read())
    n = vuln_key.n
    fdb_c =factordb.FactorDB(n)
    fdb_c.connect()
    fac_l = fdb_c.get_factor_list()
    if len(fac_l) > 1:
        p = fac_l[0]
        q = fac_l[1]
        e = vuln_key.e
        ciphertext = bytes.fromhex(open(f"{i}.ciphertext", 'r').read())
        break

d = pow(e, -1, (p-1)*(q-1))
private_key = RSA.construct((n,e,d))
cipher = PKCS1_OAEP.new(private_key)

print(cipher.decrypt(ciphertext))
