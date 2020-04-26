s=3
i=1
j=1
answer = 0
while (i+j)<=4000000 :
    
    s=i+j
    i=j
    j=s

    if s%2==0:
        answer+=s


print("짝수이면서 4백만 이하인 모든 항을 더하면 =", answer)