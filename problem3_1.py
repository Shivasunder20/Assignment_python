def solution(N):
    max = -1000000000
    for i in range(len(N)):
        for j in range(len(N)):
            for k in range(len(N)):
                if (i != j & j != k):
                    if (i != k):
                        a = N[i] * N[j] * N[k]
                        if (max < a):
                            max = a
    return max
M=int(input())
N=[]
if(M>=3 & M<=100000):
    for i in range(M):
        n=int(input())
        if(-1000<=n<=1000):
            N.append(n)
        else:
            print("Out of Range")
    print(solution(N))
else:
    print("Out of Range")