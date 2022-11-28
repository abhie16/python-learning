n1 = int(input())
n2 = int(input())
abs(n1)
abs(n2)
count = 0
mx = max(n1, n2)
mi = min(n1, n2)

if mx == mi:
    print("same input")
else:
    print("Even:")
    for i in range(mi, mx+1):
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            print(i,end=" ")
        count=0

    print("")
    print("Odd:")
    for i in range(mi, mx + 1):
        if i%2!=0:
            print(i,end=" ")