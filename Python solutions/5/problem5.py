import sys

def divisibleByAll(n,max):
    for i in range(2,max+1):
        if n%i != 0:
            return 0
    return 1

current = 1

#Find a number guaranteed to be divisible by all
for i in range(1,31):
    current *= i

numberDiv = 2

while numberDiv > 0:
    numberDiv = 0
    for i in range(2,31):
        nextNum = current/i
        if divisibleByAll(nextNum,30):
            current = nextNum
            numberDiv += 1

print current        
