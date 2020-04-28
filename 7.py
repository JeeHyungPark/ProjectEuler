#7번 문제
#10,001번째의 소수를 구하세요.
count=0
n=0
while True:
    n+=1
    t=0
    for i in range (2,n): #2부터 n-1까지 나누어 소수인지 아닌지 판별
        if n%i ==0: #소수가 아닐 경우
            break
        else: 
            t+=1
    if t==n-2: #소수일 경우
        count+=1
    if count==10001: #10001번째 소수
        break
print(n)
