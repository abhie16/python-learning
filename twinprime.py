count = 0
PrimeNumbers = []
countPrime = 0
for i in range(1,100):
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        # print(i,end=" ")
        PrimeNumbers.append(i)
        countPrime +=1
    count=0
# print(PrimeNumbers)

for k in range(0,countPrime):
    if PrimeNumbers[k] - PrimeNumbers[k-1] == 2:
        print(PrimeNumbers[k-1], 'And', PrimeNumbers[k])