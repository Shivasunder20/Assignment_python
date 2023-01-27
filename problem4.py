def solution(N):
    h = []
    s = 0
    for j in range(0, len(N)):
        if (N[j] == "1"):
            h.append(s)
            s = 0
        if (N[j] == "0"):
            s += 1
    for i in range(len(h)):
        if (s < h[i]):
            s = h[i]
    return s
N=bin(int(input())).lstrip('0h').rstrip('0')
print(solution(N))