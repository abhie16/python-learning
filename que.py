n = int(input())

if n % 9 == 0:
    print(n)
elif n<5:
    print(9)
else:
    if (9 - (n % 9)) < 5:
        print((int(n / 9)) * 9 + 9)  # (n + (9 - n%9))
    else:
        print(n - (n%9))