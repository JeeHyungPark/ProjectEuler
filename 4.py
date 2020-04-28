def find(): #답 찾는 함수
    list1=[] #대칭수 모음 list
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            a=i*j
            x=str(a) #결과값을 문자열로 변환

            if len(x)==6:
                if x[0]==x[-1] and x[1]==x[-2] and x[2]==x[-3]: #문자열 인덱스를 통해 대칭수 찾기
                    list1.append(a)
    return max(list1) #대칭수 list중에서 최고값 찾기

print(find())
    
            
        

