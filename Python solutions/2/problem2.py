def fibonnaci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

iterator = 1
sum = 0

while fibonnaci(iterator) < 4000000:
    if fibonnaci(iterator)%2 == 0:
        sum += fibonnaci(iterator)
    iterator += 1

print sum
