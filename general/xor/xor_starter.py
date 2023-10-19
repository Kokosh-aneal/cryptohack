# XOR Starter
msg = "label"

# Lambda solution
# msg = list(map(lambda i: chr(ord(i) ^ 13), msg))

# Bytes solution
msg = msg.encode("utf-8")
msg = ''.join(list(chr(b ^ 13) for b in msg))
print(msg)
    
