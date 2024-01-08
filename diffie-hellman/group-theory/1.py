import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor
from Crypto.Util.number import long_to_bytes
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def dhke_additive(base, private_key, modulus):
    return (base + private_key) % modulus

def recover_shared_key(parameters, public_key, private_key):
    modulus = int(parameters["p"], 16)
    base = int(parameters["g"], 16)
    public_key = int(public_key, 16)

    # Calculate shared key using DHKE in additive group
    shared_key = dhke_additive(public_key, private_key, modulus)
    return long_to_bytes(shared_key).rjust(16, b'\x00')  # Ensure 16-byte key

# def decrypt_flag(shared_key, ciphertext, iv):
#     key = shared_key
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
#     return decrypted.decode('utf-8')


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
        return plaintext


if __name__ == "__main__":
    # Intercepted messages
    alice_params = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff",
                    "g": "0x02"}
    bob_params = {"B": "0xd9f3a25b1754587904dcf8a7fbfad37d7faaae5ad2b64ed8bbb5408d5f36be4e1f47a0c08d3565c4702d686b76c253ea16b53135a1c1d08966edde5ddf1b77e3eb2f2960132b361ac7b4a0714942cbc21fb79279e4db26bd99262a1cf8d96ced3bcaad56b08ed5490d812d534b2823f869deffb2a734daff35321d1ce03e10cb5dc26527b3e1543d7012922f7b5443347fb8a7c74a5221706d34e59c78f736f12fa617ad04dc236029e5ab9f9cc43838e375cd6e949f95ff70e74e7f38bcc81b"}
    alice_msg = {"iv": "d8c0a85a7de7036917e3531cd634cb7f", "encrypted": "c8b7d589880cd7808fa4c686b59c09fb4d354d1638cc5678e9e2890ca903b061762db14be8e31938fc6f8fca1005e32b"}

    # Replace with your private key
    private_key_Alice = 42

    # Recover shared key
    shared_key_Alice = recover_shared_key(alice_params, bob_params["B"], private_key_Alice)
    shared_key_Alice2 = int.from_bytes(shared_key_Alice,byteorder="big")

    # Decrypt the flag
    # flag = decrypt_flag(shared_key_Alice, bytes.fromhex(alice_msg["encrypted"]), bytes.fromhex(alice_msg["iv"]))
    flag = decrypt_flag(shared_key_Alice2, alice_msg['iv'], alice_msg['encrypted'])
    print("Recovered Shared Key:", int.from_bytes(shared_key_Alice,byteorder="big"))
    print("Decrypted Flag:", long_to_bytes(int.from_bytes(flag,byteorder="big")))