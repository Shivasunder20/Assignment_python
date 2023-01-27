def no_three_consecutive(A,B):
    result=""
    while A>0 or B>0:
        if A>B:
            if result[-2:]!="aa":
                result += "a"
                A-=1
            elif B>0:
                result += "b"
                B-=1
        elif B>=A:
            if result[-2:]!="bb":
                result += "b"
                B-=1
            elif A>0:
                result +="a"
                A-=1
    return result
n=int(input())
m=int(input())
print(no_three_consecutive(n,m))