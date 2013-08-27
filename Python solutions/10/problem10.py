def isPrime(n):
    for i in range(2,n/2+1):
        if(n%i == 0):
            return 0
    return 1

primeSum = 0

for i in range(2,2000001):
    if isPrime(i):
        primeSum += i

print primeSum
