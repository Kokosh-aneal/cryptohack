from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def solve_challenge():
    while True:
        data = json_recv()
        # print(data)

        
        if "flag" in data:
            print("Flag:", data["flag"])
            break

        encoding = data["type"]
        encoded_text = data["encoded"]

        match encoding:
            case "base64":
                decoded_text = base64.b64decode(encoded_text).decode()
            case "hex":
                decoded_text = bytes.fromhex(encoded_text).decode()
            case "rot13":
                decoded_text = codecs.encode(encoded_text, 'rot_13')
            case "bigint":
                decoded_text = long_to_bytes(int(encoded_text, 16)).decode()
            case "utf-8":
                decoded_text = "".join(chr(b) for b in encoded_text)

        response = {"decoded": decoded_text}
        json_send(response)

solve_challenge()