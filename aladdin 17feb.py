def aladdin(magic,dist):
    if sum(magic)< sum(dist):return -1
    n=len(magic)
    total_val=0
    start=0
    for i in range(n):
        if total_val < 0:
            start = i
            total_val = 0
        total_val += (magic[i]-dist[i])
    return start
print(aladdin([8,4,1,9],[10,9,3,5]))