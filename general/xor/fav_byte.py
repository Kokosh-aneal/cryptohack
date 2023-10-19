import re

msg = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
msg = bytes.fromhex(msg)
for k in range(256):
    tmp_ascii = [k ^ i for i in msg]
    tmp_msg = "".join(chr(i) for i in tmp_ascii)
    if re.match("^crypto\{.*\}$",tmp_msg):
        print("msg:", tmp_msg, " | key:", k)
        break