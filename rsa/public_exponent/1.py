# e=1 => ct = pt^e MOD n = pt MOD n => pt MOD n = pt => ct = pt

ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
hexed_ct = hex(ct)

flag = bytearray.fromhex(hexed_ct[2:]).decode() # hexed_ct[2:] remove '0x' from the beginning

print(flag)