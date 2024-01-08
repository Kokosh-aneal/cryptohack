import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        # return plaintext
        return plaintext.decode('ascii')





tmp_alice = '{"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x3b127bb2fe04c9182a8b10d7fa9ff63bed71ef3b49c9d14c8fdb729d259d84489986ec4ce62fb65df1bde82948bd2f4988a31efedf315333f73ba3f0476a0eb8e291fa78e2cc186788191854a3a4b9666f48d7e7f307f2e921c4edbc111291b9cfc5bed34a27b9d897fb00f0f5c551ad33fa2ec2e17046985bcee13f41893717ad96012b0decf6f011e5ee0b1e3058226141beb54bababdfd54352db583c3f9a87397420cc9d4e954054f74c423c038b33cbb2f0afbdebd1c7497a5608238f2a"}'
alice = json.loads(tmp_alice)
# tmp_bob = '{"B": "0x1511ae1c1b230391a1beea55df834bdbc96d24a86b4e519ad1b95197874c1fb4252b999c49c8c4079f459108d6cdabcd5823940df83e370890f9c640247b1a873c9f58f8a02954590002720295c5e68cd0934f4cc4462925669c591948c26fd13bd1cdb7f9940bbb50d0ac04b6ba2a6cb2a44736047f51171e5cf3d201411751a78ccf88887017867604a6920fb1a6a8029a326c06a1bf337f137f5b765d348eb21de4d37b077f2414ff7acb401af158d03a36c9cb57ab9a54d1b08fee8a169"}'
# bob = json.loads(tmp_bob)

# Prepare alice key
a = int(alice['p'], 16) - 2
A = pow(int(alice['g'],16),a,int(alice['p'],16))
alice['A'] = hex(A)
print(json.dumps(alice))


# Prepare bob key
tmp_bob = '{"B": "0x362c8c441bb67ce5739fb6761bade61c128ed99587cb5d22ed1c1be347db2d94d8c0773e8e4bd4675e95e574fb7d6d0ba528462fa251590227eefa765998f83f3d7ca2d897fa15bc209cc8fcc6b48f7979931bbeb167344d3a49a98cb7342e67375586c8909c3469259f0c6f12bab918bdb6e885db34eb8a418aebee1e063623e94469c32f62f2c6d04daf5f2ac4ae3e4ba3b505e24e4897e2eb6413d25af773e9bc8ed0d763d724b284c4e10287d272d625d278b848e558af2689a10d9f702a"}'
bob = json.loads(tmp_bob)
b = int(alice['p'], 16) - 4
B = pow(int(alice['g'],16),b,int(alice['p'],16))
bob['B'] = hex(b)
print(json.dumps(bob))

# Decrypt message
msg = '{"iv": "14ea81e225e077ff0ea1260c61e8b0d8", "encrypted_flag": "1758e356731eb1ccf4f4662d925d945aa17e6e93090c6757cd1c675c09822155"}'
msg = json.loads(msg)
print(pow(A,b,int(alice['p'],16)))
print(decrypt_flag(pow(int(alice['A'],16),b,int(alice['p'],16)), msg['iv'], msg['encrypted_flag']))