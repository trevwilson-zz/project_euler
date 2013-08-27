for i in range(1,1001):
    for j in range(1,1001):
        if(i + j > 1000):
            break
        for k in range(1,1001):
            if(i + j + k > 1000):
                break
            elif(i*i + j*j == k*k):
                if(i + j + k == 1000):
                    print i*j*k
