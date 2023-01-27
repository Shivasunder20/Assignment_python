def isPal(num):
    if(num < 0):
        return False
    if num ==0:
        return True
    k = num
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num//10
    return k == reverse
num=int(input())
print(isPal(num))


