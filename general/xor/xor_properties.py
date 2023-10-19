# Convert keys to ints
KEY1 = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313", 16)
KEY2_xor_KEY1 = int("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", 16)
KEY2_xor_KEY3 = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", 16)
FLAG_xor_KEYS = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", 16)

# Get flag
KEY2 = KEY2_xor_KEY1 ^ KEY1
KEY3 = KEY2_xor_KEY3 ^ KEY2
FLAG = FLAG_xor_KEYS ^ KEY1 ^ KEY3 ^ KEY2

# hex to string
FLAG = hex(FLAG)[2:]  # Usuń "0x" z początku
FLAG = bytes.fromhex(FLAG).decode()

print(FLAG)