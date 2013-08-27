def isPalindrome(n):
    strN = str(n)
    for i in range(0,len(strN)/2):
        if strN[i] != strN[len(strN)-1-i]:
            return 0
    return 1

max = 0

for i in range(100,1000):
    for j in range(100,1000):
        if(isPalindrome(i*j) and i*j > max):
            max = i*j

print max
