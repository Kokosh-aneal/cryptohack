mod=13
counter = 0

while True:
    counter+1
    x = mod*counter+1
    print(counter, x)
    if x%3 == 0:
        print(x/3)
        break