def checkPrime(n):
    result = 1
    for i in range(2,n/2):
        if n%i == 0:
            result = 0
    return result

max = 0
i = 1

while i < 600851475143:
    if(600851475143%i == 0):
        if(checkPrime(i)):
            print i
            max = i
    i += 1
    
print max
            
print "done"
