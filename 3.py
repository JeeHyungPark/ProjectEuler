#3번문제
#600851475143의 소인수 중에서 가장 큰 수를 구하세요.

list1 = []
list2 = []

#나누어 떨어지는 수 들을 모두 구하여 list1에 넣는다.
for i in range(2,600851475142):
    if 600851475142 % i == 0 :
        list1.append(i)
    
#list1안에서 소인수를 찾는다.
for j in list1:
    t=0
    for n in range(2,j-1):
        if j%n == 0:
            t+=1
    if t==0:
        list2.append(j)

print(list2[-1])
            
            
