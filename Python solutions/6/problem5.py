sum = 0
squareSum = 0

for i in range(1,101):
    sum += i
    squareSum += i*i

sumSquared = sum*sum

print sumSquared-squareSum
