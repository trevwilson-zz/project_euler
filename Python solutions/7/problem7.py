def isPrime(n):
    for i in range(2,n/2+1):
        if(n%i == 0):
            return 0
    return 1

primeCount = 0
iterator = 2

while(primeCount != 10001):
    if isPrime(iterator):
        primeCount += 1
    iterator += 1

print iterator
