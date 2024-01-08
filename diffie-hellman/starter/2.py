# def is_generator(k, p):
#   for n in range(2, p):
#     if pow(k, n, p) == k:
#       return False
#   return True

# p = 28151
# for k in range(p):
#   if is_generator(k, p):
#     print(k)
#     break

# Primitive root => Obdisian
p = 28151
for k in range(p):
    tmp = int((p-1)/2)
    if pow(k,tmp,p) == p-1:
        print(k)
        break

