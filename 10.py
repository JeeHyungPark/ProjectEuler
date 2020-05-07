# 2,000,000 이하 소수의 합은 얼마 입니까?

def sosu(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

def answer(n):
    sum = 17
    for i in range(10, n+1):
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
            if sosu(i):
                sum += i
        i += 2
    return sum

print(answer(2000000))
