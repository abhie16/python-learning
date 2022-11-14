# series A/13 + B/14 + E/17 + G/22 and so on

A = 65

for x in range(0, 10):
    character = chr(A)
    print(character, "/", (13+(x*x)), end=" ")  # here end work as enter
    if x == 9:
        break
    else:
        print(" + ", end=" ")
    A += 2