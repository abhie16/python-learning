import random

correctAns = 0
for i in range(0,5):
    a = int(random.random()*100)
    b = int(random.random()*100)
    print(a," + ",b)
    ans = int(input("Enter your answer: "))

    if ans == a+b:
        correctAns += 1
print("Number of correct anss: ", correctAns)
